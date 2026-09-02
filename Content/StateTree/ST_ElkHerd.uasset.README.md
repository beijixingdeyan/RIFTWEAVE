# ST_ElkHerd (StateTree)
- **States**: Graze -> Migrate -> Panic (broadcast) -> Flee -> Calm
- **Tasks**: MoveTo, PlayAnim, BroadcastPanic (30m, decay 0.9)
- **Evaluators**: BiomeBlend (threshold 0.5), InRift (tag)
- **Transitions**: Panic signal -> Flee, Light > 0.7 -> Migrate
- **Mass**: 2000 entities, 30Hz, dormancy >120m via ReplicationGraph
- **Nanite**: N/A (StateTree, not mesh)
