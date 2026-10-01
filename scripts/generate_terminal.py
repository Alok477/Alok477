import shutil
from pathlib import Path

import gifos

ROOT = Path(__file__).resolve().parents[1]

# Install the TOML configuration where gifos expects it
config_dir = Path.home() / ".config" / "gifos"
config_dir.mkdir(parents=True, exist_ok=True)

shutil.copy2(
    ROOT / ".github" / "gifos_settings.toml",
    config_dir / "gifos_settings.toml",
)

# Create terminal
t = gifos.Terminal(
    width=640,
    height=320,
    xpad=10,
    ypad=10,
)

# Get Alok477's GitHub stats
github_stats = gifos.utils.fetch_github_stats(
    user_name="Alok477"
)

# Terminal content
t.gen_text(
    "╭─[ Alok477@github ]",
    row_num=1,
)

t.gen_text(
    "╰─$ neofetch",
    row_num=2,
)

t.gen_text(
    f"User       : {github_stats.account_name}",
    row_num=4,
)

t.gen_text(
    "OS         : GitHub",
    row_num=5,
)

t.gen_text(
    "Shell      : bash",
    row_num=6,
)

t.gen_text(
    "Languages  : Python / JavaScript / TypeScript",
    row_num=7,
)

t.gen_text(
    "Status     : Building things 🚀",
    row_num=8,
)

t.gen_text(
    "GitHub     : github.com/Alok477",
    row_num=9,
)

t.gen_text(
    "╰─$ ",
    row_num=11,
)

# Generate output.gif
t.gen_gif()
