FROM fluent/fluentd:v1.16-1

USER root

RUN apk add --no-cache --update \
      build-base \
      ruby-dev \
      && gem install fluent-plugin-kafka -v 0.19.1 --no-document

USER fluent