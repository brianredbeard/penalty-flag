# Penalty Flag

A colorful custom error pages server for use with the NGINX ingress controller
for Kubernetes.

| Container Path | Status | 
| -------------- | ------ |
| quay.io/brianredbeard/penalty-flag   |  [![Docker Repository on Quay](https://quay.io/repository/brianredbeard/penalty-flag/status "Docker Repository on Quay")](https://quay.io/repository/brianredbeard/penalty-flag) |
| quay.io/brianredbeard/penalty-flag-amd64   |  [![Docker Repository on Quay](https://quay.io/repository/brianredbeard/penalty-flag-amd64/status "Docker Repository on Quay")](https://quay.io/repository/brianredbeard/penalty-flag-amd64) |
| quay.io/brianredbeard/penalty-flag-arm   |  [![Docker Repository on Quay](https://quay.io/repository/brianredbeard/penalty-flag-arm/status "Docker Repository on Quay")](https://quay.io/repository/brianredbeard/penalty-flag-arm) |
| quay.io/brianredbeard/penalty-flag-arm64   |  [![Docker Repository on Quay](https://quay.io/repository/brianredbeard/penalty-flag-arm64/status "Docker Repository on Quay")](https://quay.io/repository/brianredbeard/penalty-flag-arm64) |
| quay.io/brianredbeard/penalty-flag-ppc64le   |  [![Docker Repository on Quay](https://quay.io/repository/brianredbeard/penalty-flag-ppc64le/status "Docker Repository on Quay")](https://quay.io/repository/brianredbeard/penalty-flag-ppc64le) |

# About

Penalty Flag is a custom error page server derived from the upstream example
within the Kubernetes [NGINX Ingress][nginx-ingress] repository.

The idea is that, in the same way that the color of a referee's flag bears
meaning for particpants and spectators of a football game, this custom error
server provides more colorful (and generally useful) "flags" when something goes
wrong with a request processed by ingress.

# Screenshots

![404 error screenshot](docs/screenshots/404.png)

![508 error screenshot](docs/screenshots/508.png)

![418 error screenshot](docs/screenshots/418.png)

![306 error screenshot](docs/screenshots/306.png)

<!--
# Setup

# Troubleshooting

# Development

-->
[nginx-ingress]: https://github.com/kubernetes/ingress-nginx
<!--
vim: ts=2 sw=2 et tw=80
-->
