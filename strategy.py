#!/usr/bin/env python3
# Place a single KO market buy order using CPZ AI keys from environment.

import os
import sys
from cpz.clients.sync import CPZClient

# --- Set credentials ---
os.environ["CPZ_AI_API_KEY"] = "cpz_key_6ee65f4ef5bf4d63a93a60c1"
os.environ["CPZ_AI_SECRET_KEY"] = "cpz_secret_4e1k6i3b435j341d3a4tp2r5d4t632vkn163h3t45213v27w"
os.environ["CPZ_STRATEGY_ID"] = "8b5bebeb-9a07-4de5-b6d4-0fadfb5665ec"

# --- Direct argument values ---
qty = 1
strategy_id = os.getenv("CPZ_STRATEGY_ID")
env = "paper"         # choose "paper" or "live"
broker = "alpaca"     # choose broker name
# --- Validation ---
if not os.getenv("CPZ_AI_API_KEY") or not os.getenv("CPZ_AI_SECRET_KEY"):
    print("CPZ_AI_API_KEY and CPZ_AI_SECRET_KEY must be set in environment", file=sys.stderr)
    sys.exit(2)

if not strategy_id:
    print("--strategy-id (or CPZ_STRATEGY_ID) is required", file=sys.stderr)
    sys.exit(2)

# --- Execute order ---
client = CPZClient()
client.execution.use_broker(broker, account_id="PA3FHUB575J3")

order = client.execution.order(
    symbol="KO",
    qty=qty,
    side="buy",
    order_type="market",
    time_in_force="DAY",
    strategy_id=strategy_id,
)

print(order.model_dump_json())
