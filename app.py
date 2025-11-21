from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

import numpy as np
from flask import Flask, render_template, request


@dataclass
class OptionInputs:
    spot_price: float
    strike_price: float
    maturity: float
    risk_free_rate: float
    volatility: float
    simulations: int
    time_steps: int
    option_type: str


def simulate_payoff(params: OptionInputs) -> float:
    dt = params.maturity / params.time_steps
    discount_factor = math.exp(-params.risk_free_rate * params.maturity)
    payoffs = []

    for _ in range(params.simulations):
        prices = [params.spot_price]
        for _ in range(params.time_steps):
            z = np.random.normal()
            next_price = prices[-1] * math.exp(
                (params.risk_free_rate - 0.5 * params.volatility ** 2) * dt
                + params.volatility * math.sqrt(dt) * z
            )
            prices.append(next_price)

        terminal_price = prices[-1]
        if params.option_type == "call":
            payoffs.append(max(terminal_price - params.strike_price, 0))
        else:
            payoffs.append(max(params.strike_price - terminal_price, 0))

    return discount_factor * float(np.mean(payoffs))


def parse_form(form_data) -> Optional[OptionInputs]:
    try:
        option_type = form_data.get("option_type", "call")
        return OptionInputs(
            spot_price=float(form_data.get("spot_price", 100)),
            strike_price=float(form_data.get("strike_price", 100)),
            maturity=float(form_data.get("maturity", 1)),
            risk_free_rate=float(form_data.get("risk_free_rate", 0.05)),
            volatility=float(form_data.get("volatility", 0.2)),
            simulations=int(form_data.get("simulations", 10000)),
            time_steps=int(form_data.get("time_steps", 252)),
            option_type=option_type if option_type in {"call", "put"} else "call",
        )
    except (TypeError, ValueError):
        return None


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    params = parse_form(request.form) if request.method == "POST" else None

    if request.method == "POST":
        if params is None:
            error = "모든 숫자 입력이 올바르게 채워졌는지 확인하세요."
        elif params.simulations <= 0 or params.time_steps <= 0 or params.maturity <= 0:
            error = "시뮬레이션 횟수, 타임스텝, 만기는 0보다 커야 합니다."
        else:
            result = simulate_payoff(params)

    display_params = params or OptionInputs(
        spot_price=100,
        strike_price=100,
        maturity=1,
        risk_free_rate=0.05,
        volatility=0.2,
        simulations=10000,
        time_steps=252,
        option_type="call",
    )

    return render_template("index.html", result=result, error=error, params=display_params)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
