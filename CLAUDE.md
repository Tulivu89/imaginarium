# Imaginarium

NovelAI Diffusion V5 prompt writing for a video game's art. The rules (session mode, scope, commands) are in the system prompt: the **Imaginarium** output style (`.claude/output-styles/imaginarium.md`), selected in `.claude/settings.json`. If this session isn't running that style, read that file before any image turn and follow it.

**Session mode.** Each chat session is SFW (the default; any ages, kids included, nothing suggestive) or mature (adult content open; no child or teen character involved at all). Ask on the first message if the user hasn't said, and keep it for the session.

- **`nai-v5-images`** (`.claude/skills/`) handles every image request: briefs, character looks, sprites, CGs, key art, pose modules. Its `references/` hold tags, artists, style blocks, UC presets, positioning, face kits, body kits and poses.
- **Look notes:** `Characters/<Name>.md`, from `Characters/_Look template.md`. Every character carries `age` and `stage`; nonhumans carry `mind`.
- **Saved setups:** `Scenes/<Title>.md`; mature-session setups in `Scenes/Mature/`. Generated images: `Images/<Name or Title>/`; mature ones in `Images/Mature/`.

## Game look

*Fill in once the art direction is set: the style block every asset uses, default resolution, background rule for sprites.*

- Style block: (none yet)
- Default size: (none yet)

## Git

Pull before editing. Commit saved looks and setups with short messages (`Looks: <name>`, `Scene: <title>`, `Poses: <change>`) and push.
