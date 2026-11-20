# Imaginarium

Claude Code setup for writing NovelAI Diffusion V5 prompts for the game's art.

## Use it

1. Open this repo in Claude Code (web at claude.ai/code, desktop or CLI).
2. Claude asks once per session whether it's a **mature-content session**. *No* (SFW) allows every character, kids included, with nothing suggestive. *Yes* opens adult content, and no child or teen characters can be involved for that session. Start a new session to switch.
3. Ask for an image: `[img: <who>, <where>, <mood>, <what the asset is for>]`, or plain English ("sprite of the blacksmith, neutral and angry").
4. Paste the setup into NovelAI: Model & Settings, Base Prompt, Base UC, then one Character Prompt and UC per character.
5. `[save]` keeps a setup or look; `[look: <Name>]` builds a character's look note so every later image matches.

The full rules are in `.claude/output-styles/imaginarium.md`.

## What's here

| Path | Holds |
|---|---|
| `.claude/skills/nai-v5-images/` | The V5 rulebook and its references (tags, artists, style blocks, face and body kits, poses) |
| `Characters/` | Look notes, one per character |
| `Scenes/` | Saved setups (`Mature/` for mature sessions) |
| `Images/` | Generated images (`Mature/` for mature sessions) |
