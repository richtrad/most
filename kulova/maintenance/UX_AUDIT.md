# Kulová: UX and consistency audit, 3 October 2026

Scope: street index, houses 257, 259, 261, 263, 264, archived 264,
their Czech/English pages, and the two comparison laboratories (16 routes).
Source baseline: published main 6a26caaf1145fb8f8a21612ce13888aab74637f7.

## Findings and changes

1. No active-house indication; language and return links varied by page.
   Added a shared, labelled street navigation, current-house state, consistent
   language switch and return links. Archived 264 is explicitly identified and
   linked to the corrected version. Existing public routes remain intact.
2. A text-only street list gave no visual way to identify a reconstruction.
   Added five lightweight thumbnails from the actual baseline viewer screenshots
   and distinct process summaries. Colour/detail hypotheses remain explicit.
3. Long process articles offered no complete chapter overview.
   Added static, collapsible contents lists and persistent heading IDs, including
   absolute page anchors so the English pages' base URLs cannot misroute them.
4. Raw view names (hero, axis_front, opening_U4_left) exposed internal codes.
   Added Czech/English human-readable camera labels without changing camera keys
   or positions. Kept diagnostic opening identifiers and all views available.
5. Sliders overlaying pictures, missing side labels, and inconsistent drag
   behaviour made before/after comparisons hard to use, especially on touch.
   Added side captions and dividers to older widgets, moved overlaid sliders
   below their images, and enabled horizontal dragging plus keyboard input.
   The existing registered-photo comparison on 261 is retained. Its long labels
   now wrap rather than overlap on mobile. Dynamic comparisons are enhanced too.
6. Fonts, control sizes, model heights, focus states and instructions differed.
   Added a common presentation layer, wrapping controls, minimum 44px controls,
   reduced-motion support, keyboard skip links and model/slider instructions.
   Source dialogs and static comparisons work independently of model loading.
   On narrow screens, a native disclosure collapses the large control panel so
   the model appears sooner. Desktop controls remain open; every setting and
   the source dialog are available after expanding the mobile disclosure.
7. Laboratory copy still described C/G selection as pending.
   Updated method status: C was chosen; G is the default after source checking;
   T is an explicitly requested alternative. Preserved all experimental models
   and the original main 261 model. No historical approval was inferred.

## Evidence

`before/` and `after/` contain desktop/mobile browser screenshots and audit JSON.
`load-validation/` contains model/source-dialog/mobile screenshots and checks
for broken local dependencies, duplicate IDs and mobile overflow on 14 routes.
The behavioural audit additionally exercises dragging, keyboard sliders,
chapter anchors and both laboratories. Deployment evidence is recorded after
publishing. No geometry, textures, source photographs or QA approvals changed.

## Regeneration

The published HTML is an export from separate house reconstruction bundles.
After rebuilding the publication with `kulova_publish_20261002/prepare.py`,
run its path correction step, retain the shared `most/kulova/ux.css`, `ux.js`
and five `assets/house-*.jpg`, then apply this idempotent layer:

    python output/kulova_ux_20261003/apply_ux.py --root PATH_TO_PUBLICATION_REPO

The root argument prevents changes to another checkout. Preserve the exported
model/source files and inspect the focused diff before publication.
