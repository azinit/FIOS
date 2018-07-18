import FIOS.cfg as cfg

#   FIOS
assistant = cfg.get(cfg.iCore, "General", "assistant")
assistant_full = cfg.get(cfg.iCore, "General", "assist_transcript")
user = cfg.get(cfg.iCore, "General", "user")
width = int(cfg.get(cfg.iCore, "General", "line_amount"))
TESTPHRASE = cfg.get(cfg.iCore, 'Add', 'test')