# tier_enforcer

This engine enforces the AI.Web Tiered Communication Framework.

It analyzes output and:
- Classifies it as Tier 1, Tier 2, or Mixed
- Logs violations to `tier_violation_log.json`
- Tags clean content with `[TIER 1]` or `[TIER 2]` headers
- Blocks mixed or unclassified output to prevent interface drift

This engine ensures runtime voice coherence across all LLMs and agents.
