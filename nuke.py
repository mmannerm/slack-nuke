#!/usr/bin/env python3

import yaml

from slack_cleaner2 import *

with open("config.yml", "r") as configfile:
  cfg = yaml.load(configfile, Loader=yaml.BaseLoader)

f = is_not_pinned()
before = a_while_ago(days=13)

for token in cfg["tokens"]:
  s = SlackCleaner(token)
  s.sleep_for = 1.0

  with s.log.group("files"):
    for entry in filter(f, s.files(before=before)):
      entry.delete()

  for c in s.conversations:
    with s.log.group(c.name):
      for msg in filter(f, c.msgs(before=before)):
        if (c.type.value != 4) or (msg.user == s.myself):
          msg.delete(as_user=True, files=True, replies=True)

  s.log.summary()
