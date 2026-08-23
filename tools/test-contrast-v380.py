#!/usr/bin/env python3
"""Regression checks for confirmed small-text contrast failures."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "assets/styles/main.css").read_text(encoding="utf-8")


def luminance(rgb: tuple[int, int, int]) -> float:
    channels = []
    for value in rgb:
        normalized = value / 255
        channels.append(normalized / 12.92 if normalized <= 0.04045 else ((normalized + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast(foreground: tuple[int, int, int], background: tuple[int, int, int]) -> float:
    light, dark = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


background = (8, 47, 35)
foreground = tuple(round(0.72 * 255 + 0.28 * value) for value in background)
assert contrast(foreground, background) >= 4.5, "copyright do rodapé abaixo de 4,5:1"
assert "color: rgba(255, 255, 255, 0.72);" in CSS, "cor acessível do copyright ausente"
assert ".chatbot-header button {" in CSS and "color: var(--verde-escuro);" in CSS, "botão do Max sem contraste no cabeçalho claro"
print("CONTRAST_V380_OK")
