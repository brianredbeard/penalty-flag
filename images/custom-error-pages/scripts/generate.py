#!/usr/bin/env python
"""generate.py - generate custom status pages

Copyright 2020 Brian 'redbeard' Harrington
Originally copyright 2018 Denys Vitali

This utility will retrieve the current HTTP status codes and generate a
complete list of well formatted pages to be used with NGINX, Kubernetes Ingress
controllers, and other similar systems.

It is originally derived from multiple open source projects:

  - "nginx-error-pages" project by Denys Vitali:
    https://github.com/denysvitali/nginx-error-pages

  - "custom-error-pages" project within the community maintained NGINX ingress
  for Kubernetes:
    https://github.com/kubernetes/ingress-nginx/tree/master/images/custom-error-pages

"""

import json
import os
import requests

PREFIXPATH = os.getenv("ERR_PATH", '../rootfs/www/')

BASE = (os.path.dirname(__file__))

# Use the file "css.json" to populate various style information, as well as
# to embed the teapot image and other relevant info.  The intention was just
# to consolidate the "configuration" into a single structure, easier for
# subsequent developers to understand.
with open(os.path.join(BASE, 'css.json')) as c:
    CSS = json.load(c)

# Thanks to Erik Wilde (@dret) for maintaining the WebConcepts project,
# enabling projects like this one.
# This provides all codified http status codes in a structure we can iterate
# over to create the relevant status pages.
CODES = requests.get('http://webconcepts.info/concepts/http-status-code.json')
JSONSTATUS = CODES.json()

for i in JSONSTATUS["values"]:
    # Extract the first digit of the error code and suffix with xx
    p = i["value"][0:1] + "xx"

    # Use the following template file to generate the various error pages
    template = os.path.join(BASE, "template.html")
    with open(template) as f:
        content = f.read()
        new_content = content
        error_code = int(i["value"])

        image = CSS['images'].get(str(error_code), "")

        description = CSS['description'].get(str(error_code),
                                             i["details"][0]["description"])

        # Provide a CSS "override".  In reality, this is used to populate the
        # class for the outer div on the 418 overlay, but keeping this here
        # allows us to greatly simplify the templating process at the expense
        # of a slight increase in complexity in css.json
        override = CSS['override'].get(str(error_code), "")

        # Extract relevant information on the RFC which originates the error
        # code.  If both the spec-name and documentation fields are *not*
        # empty, generate the paragraph tag to be embedded in the page.
        spec = i["details"][0].get("spec-name", "")
        documentation = i["details"][0].get("documentation", "")
        if len(spec) > 0 and len(documentation) > 0:
            details = "<p class='spec'>As defined in: "
            "<a href='{}'>{}</a></p>".format(documentation, spec)

        # If there is an image for the specified error code (e.g. 418)
        # Create a CSS structure with which to embed the data inline in the
        # response
        if len(image) > 0:
            image = "html{ background-image:" + image + ";"
            "background-size: cover; background-position: 50% 50%; }"

        new_content = new_content.replace("$ERROR_CODE", i["value"])
        new_content = new_content.replace("$ERROR_NAME", i["description"])
        new_content = new_content.replace("$ERROR_DESC", description)
        new_content = new_content.replace("$BGCOLOR", CSS['background'][p])
        new_content = new_content.replace("$CSS_STYLE", CSS['style'])
        new_content = new_content.replace("$OVERRIDE", override)
        new_content = new_content.replace("$IMAGE", image)
        new_content = new_content.replace("$DETAILS", details)

        # Output the HTML pages to the desired directory
        fname = os.path.join(PREFIXPATH, i["value"] + ".html")
        with open(fname, "w") as output_file:
            output_file.write(new_content)

        # Create a JSON payload for each file, in the event that the default
        # backend needs the info in a different format.
        f = {"code": error_code, "name": i["description"],
             "message": description}
        fname = os.path.join(PREFIXPATH, i["value"] + ".json")
        with open(fname, "w") as output_file:
            json.dump(f, output_file)
