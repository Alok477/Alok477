import shutil
from pathlib import Path

import gifos

ROOT = Path(__file__).resolve().parents[1]
config_src = ROOT / ".github" / "gifos_settings.toml"
config_dir = Path.home() / ".config" / "gifos"
config_dir.mkdir(parents=True, exist_ok=True)
shutil.copy2(config_src, config_dir / "gifos_settings.toml")

t = gifos.Terminal(width=640, height=320, xpad=14, ypad=14, font_size=16)
t.set_fps(15)
t.set_loop_count(0)

t.gen_typing_text("\x1b[1;36m$ whoami\x1b[0m", row_num=1, speed=2)
t.gen_text("alok477", row_num=2)

t.gen_typing_text("\x1b[1;36m$ cat profile.txt\x1b[0m", row_num=4, speed=2)
t.gen_text([
    "\x1b[1;35mAlok Kumar\x1b[0m",
    "Computer Science Student",
    "Web Developer • Python • React • FastAPI",
    "Building projects, learning in public.",
], row_num=5)

t.gen_typing_text("\x1b[1;36m$ github --stats\x1b[0m", row_num=10, speed=2)

stats = gifos.utils.fetch_github_stats(
    user_name="Alok477",
    include_all_commits=False,
)

if stats:
    t.gen_text([
        f"followers    : {stats.total_followers}",
        f"stars        : {stats.total_stargazers}",
        f"commits      : {stats.total_commits_last_year}",
        f"pull requests: {stats.total_pull_requests_made}",
        f"issues       : {stats.total_issues}",
        f"rank         : {stats.user_rank}",
    ], row_num=11)
else:
    t.gen_text("Unable to fetch live GitHub stats.", row_num=11)

t.gen_text("\x1b[1;32m$ ready_\x1b[0m", row_num=18)
t.gen_gif()
