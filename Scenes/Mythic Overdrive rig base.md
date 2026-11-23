# Mythic Overdrive rig base

SFW. Test hero for the paper-doll rig (rig template v1: A-pose, front three-quarter, 8 heads, flat key colors). Importable PNGs sit beside this file: drag one into NovelAI and choose Import (untick Seed).

Built from the user's 2026-11-23 runs (seeds 1262331755, 2097888072, 3626603972), which added the Valorant / dan mora / obj shep reference block and the artist UC. v3 changes: no shadow tone (the far leg and boot came out as different colors), arms at about 20°, 8-head cue, mitten hands, rounded boot toes, the lineless UC no longer negates `no lineart`, no `mature female`.

## A outlined

**Model & Settings**
```
Model: NovelAI Diffusion V5 Full (Anime) | Effort: High
Sampler: Euler Ancestral (karras) | Steps: 28 | Guidance: 4.5 | Rescale: 0.1
Resolution: 832x1216 (Normal portrait), then NovelAI upscale to reach 1800+ px | Seed: random
Quality Tags toggle: OFF | UC Preset: None
```

**Base Prompt**
```
1girl, solo, transparent background, full body, standing, 1.3::a-pose::, legs apart, looking at viewer, closed mouth, superhero costume, -1::close-up::. Hero stands upright in A-pose at center of image, torso, hips and feet turned partway toward right side of image in three-quarter view, near shoulder and hip wider, far shoulder and hip narrower, face turned slightly toward viewer. Both arms angle outward from shoulders like sides of letter A, each hand held one forearm-length away from thigh, wide open gap between each arm and torso. Both arms fully visible from shoulder to fingertips, far arm included. Hands are simple open mitten shapes, fingers pressed together, thumb resting along index finger, palms facing thighs. Feet planted slightly wider than hips, legs straight, open gap between legs, both legs fully visible from hip to sole. Boots end in rounded toes, both feet flat on ground. Small head and long legs: head is one eighth of total height, hips sit at middle of figure. Whole figure fits inside image with margin above hair and below boot soles.

0.8::thick lineart, flat color, Clean vector comic-book character art for 2D game, crisp and simple like vector illustration exported from design software. Bold smooth black outlines of even width trace outer silhouette of figure and border of every color area: hair, face, neck, bodysuit, leotard, gloves, belt and boots. Outer silhouette line is slightly heavier than interior lines. Every outline is one clean unbroken stroke with steady width, closed around its shape like vector path. Every line sits on border between two color areas or marks facial feature, so interior of each color area stays open, clean and flat. Facial features use few simple lines: upper eyelid, iris, pupil, eyebrow, small nose line and short mouth line. Color is flat and graphic. Every color area is one loud saturated key color with even value from edge to edge. Near and far limbs share identical color: both legs match, both gloves match, both boots match. Light is flat and even. Shape language is simple and heroic. Forms are smooth tapered shapes with gentle curves and clean silhouettes, small details merged into larger shapes, readable at small size. Muscles and fabric folds are carried by silhouette alone. Neck clear, shoulders defined, limbs long and tapered, boots sturdy and planted. Face is stylized western cartoon: moderately small almond eyes with solid colored iris and dark pupil, solid eyebrows, small simple nose, short mouth line, smooth jaw. ::

2::copyright:valorant,:: 1.5::artist:dan mora::, 1.0::artist:obj shep::,

0.8::copyright:wuthering waves::, 0.6::copyright:arknights: endfield::, 0.5::copyright:dislyte::, official art, official style,

year 2026, rating:general, medium complexity
```

**Base UC**
```
1::artist:urushihara satoshi, artist:shirow masamune,::

artist:yone kinji, blender (medium),

lowres, artistic error, scan artifacts, worst quality, bad quality, jpeg artifacts, multiple views, very displeasing, too many watermarks, nsfw, no lineart, colored lineart, anime coloring, realistic, semi-realistic, 3d, painterly, traditional media, sketch, hatching (texture), screentone, halftone, gradient background, shiny skin, shiny clothes, perspective, foreshortening, from above, from below, dutch angle, motion lines, speed lines, white outline, character outer glow, aura, chibi, big head
```

**Character 1**
```
girl, tall female. Warm light peach skin.
short hair, bob cut, swept bangs, brown hair. Medium chocolate brown hair ends above jawline, clear of neck and shoulders.
green eyes,
medium breasts. Athletic build, defined shoulders, long arms.
long legs.
blue bodysuit. Bright medium blue bodysuit covers arms and legs as smooth unbroken blue areas.
red leotard, sleeveless, turtleneck leotard. Pure bright red leotard worn over bodysuit covers torso from neck to hips as one smooth unbroken red area.
yellow gloves. Bright lemon yellow gloves fit closely over hands and reach mid-forearm, ending in clean straight edge.
yellow belt. Plain lemon yellow belt circles waist.
yellow boots, knee boots. Bright lemon yellow boots reach just below knees, low flat heels, rounded toes.
```

**Character 1 UC**
```
petite, plump, muscular female, abs, thick thighs, large breasts, cleavage, covered nipples, covered navel, impossible clothes,
blonde hair, black hair, red hair, long hair, twintails, ponytail, blue eyes, brown eyes,
dark-skinned female, pale skin,
multicolored bodysuit, two-tone bodysuit, mismatched legwear, mismatched gloves, mismatched footwear,
emblem, cape, zipper, buckle, straps, buttons, frills, armor, knee pads, thigh strap, garter straps, necklace, jewelry, goggles, mask, hair ornament, highleg leotard, skirt, high heel boots, platform boots,
spread fingers, claw pose,
```

## B lineless

**Model & Settings**
```
Model: NovelAI Diffusion V5 Full (Anime) | Effort: High
Sampler: Euler Ancestral (karras) | Steps: 28 | Guidance: 4.5 | Rescale: 0.1
Resolution: 832x1216 (Normal portrait), then NovelAI upscale to reach 1800+ px | Seed: random
Quality Tags toggle: OFF | UC Preset: None
```

**Base Prompt**
```
1girl, solo, transparent background, full body, standing, 1.3::a-pose::, legs apart, looking at viewer, closed mouth, superhero costume, -1::close-up::. Hero stands upright in A-pose at center of image, torso, hips and feet turned partway toward right side of image in three-quarter view, near shoulder and hip wider, far shoulder and hip narrower, face turned slightly toward viewer. Both arms angle outward from shoulders like sides of letter A, each hand held one forearm-length away from thigh, wide open gap between each arm and torso. Both arms fully visible from shoulder to fingertips, far arm included. Hands are simple open mitten shapes, fingers pressed together, thumb resting along index finger, palms facing thighs. Feet planted slightly wider than hips, legs straight, open gap between legs, both legs fully visible from hip to sole. Boots end in rounded toes, both feet flat on ground. Small head and long legs: head is one eighth of total height, hips sit at middle of figure. Whole figure fits inside image with margin above hair and below boot soles.

no lineart, flat color, Clean graphic vector character art for 2D game, built from flat solid matte color shapes with crisp smooth edges, like vector illustration exported from design software. Shapes meet edge to edge, and each boundary is defined by change of color between neighboring areas. Thin dark lines appear only for facial features: upper eyelid, iris, pupil, eyebrow, small nose line and short mouth line. Color is flat and graphic. Every color area is one loud saturated key color with even value from edge to edge. Near and far limbs share identical color: both legs match, both gloves match, both boots match. Light is flat and even. Shape language is simple and heroic. Forms are smooth tapered shapes with gentle curves and clean silhouettes, small details merged into larger shapes, readable at small size. Muscles and fabric folds are carried by silhouette alone. Neck clear, shoulders defined, limbs long and tapered, boots sturdy and planted. Face is stylized western cartoon: moderately small almond eyes with solid colored iris and dark pupil, solid eyebrows, small simple nose, short mouth line, smooth jaw.

2::copyright:valorant,:: 1.5::artist:dan mora::, 1.0::artist:obj shep::,

0.8::copyright:wuthering waves::, 0.6::copyright:arknights: endfield::, 0.5::copyright:dislyte::, official art, official style,

year 2026, rating:general, medium complexity
```

**Base UC**
```
1::artist:urushihara satoshi, artist:shirow masamune,::

artist:yone kinji, blender (medium),

lowres, artistic error, scan artifacts, worst quality, bad quality, jpeg artifacts, multiple views, very displeasing, too many watermarks, nsfw, thick lineart, colored lineart, anime coloring, realistic, semi-realistic, 3d, painterly, traditional media, sketch, hatching (texture), screentone, halftone, gradient background, shiny skin, shiny clothes, perspective, foreshortening, from above, from below, dutch angle, motion lines, speed lines, white outline, character outer glow, aura, chibi, big head
```

**Character 1**
```
girl, tall female. Warm light peach skin.
short hair, bob cut, swept bangs, brown hair. Medium chocolate brown hair ends above jawline, clear of neck and shoulders.
green eyes,
medium breasts. Athletic build, defined shoulders, long arms.
long legs.
blue bodysuit. Bright medium blue bodysuit covers arms and legs as smooth unbroken blue areas.
red leotard, sleeveless, turtleneck leotard. Pure bright red leotard worn over bodysuit covers torso from neck to hips as one smooth unbroken red area.
yellow gloves. Bright lemon yellow gloves fit closely over hands and reach mid-forearm, ending in clean straight edge.
yellow belt. Plain lemon yellow belt circles waist.
yellow boots, knee boots. Bright lemon yellow boots reach just below knees, low flat heels, rounded toes.
```

**Character 1 UC**
```
petite, plump, muscular female, abs, thick thighs, large breasts, cleavage, covered nipples, covered navel, impossible clothes,
blonde hair, black hair, red hair, long hair, twintails, ponytail, blue eyes, brown eyes,
dark-skinned female, pale skin,
multicolored bodysuit, two-tone bodysuit, mismatched legwear, mismatched gloves, mismatched footwear,
emblem, cape, zipper, buckle, straps, buttons, frills, armor, knee pads, thigh strap, garter straps, necklace, jewelry, goggles, mask, hair ornament, highleg leotard, skirt, high heel boots, platform boots,
spread fingers, claw pose,
```
