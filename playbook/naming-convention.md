# Ad naming convention

Reports can only match results to angles if the ad name carries the angle. Use the **same code** in the brief, the
Studio ad code note, and the Meta ad name.

```
<SEGMENT>_<ANGLE>_<PERSONA>_<FORMAT>_<HOOK>_<VERSION>
GLP1_A01_P1_UGC_H2_v1
GLP1_A22_P3_AUTH_H1_v2
```

| Part | Meaning | Values |
|---|---|---|
| SEGMENT | Which research segment | `GLP1`, `MENO` |
| ANGLE | Angle number from `idea-bank` / research §9.3 | `A01` … `A28` (new angles continue the numbering) |
| PERSONA | Persona / sub-avatar | `P1` … `P7` (research §4.9; see `personas/`) |
| FORMAT | Format code | `UGC`, `DRAMA`, `ANIM`, `SONG`, `AUTH` (authority explainer), `STAT` (static), `NAT` (native) |
| HOOK | Which hook variation | `H1`, `H2` … |
| VERSION | Iteration number | `v1`, `v2` … |

Rules: no spaces, underscores only, keep the order. If an ad is an iteration, the version goes up and the brief
says what changed.
