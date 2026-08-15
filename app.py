import streamlit as st
import numpy as np
from scipy.stats import norm

@st.cache_data
def black_scholes_greeks(S, K, T, r, sigma, q, option_type):
    """
    Calcule prix et grecques pour une option Européenne (Call ou Put)
    S : sous-jacent, K : strike, T : temps à échéance (années)
    r : taux sans risque, sigma : vol, q : dividende continu
    option_type : "Call" ou "Put"
    """
    # Cas limite T = 0
    if T <= 0:
        if option_type == "Call":
            price = max(S - K, 0.0)
            delta = 1.0 if S > K else 0.0
        else:
            price = max(K - S, 0.0)
            delta = -1.0 if S < K else 0.0
        # Les autres grecques sont nulles ou non définies
        return price, delta, 0.0, 0.0, 0.0, 0.0

    # Éviter division par zéro
    sigma = max(sigma, 1e-8)

    # Calcul des d1 et d2
    sqrtT = np.sqrt(T)
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT

    # Prix
    if option_type == "Call":
        price = S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        delta = np.exp(-q * T) * norm.cdf(d1)
        rho   =  K * T * np.exp(-r * T) * norm.cdf(d2) / 100
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)
        delta = -np.exp(-q * T) * norm.cdf(-d1)
        rho   = -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100

    # Grecques communes
    gamma = np.exp(-q * T) * norm.pdf(d1) / (S * sigma * sqrtT)
    vega  = S * np.exp(-q * T) * sqrtT * norm.pdf(d1) / 100

    # Theta par jour (division par 365)
    # pour Call : -(Sσφ/(2√T)) + qSΦ - rKΦ
    # pour Put  : -(Sσφ/(2√T)) - qSΦ(-d1) + rKΦ(-d2)
    theta_term = -S * sigma * np.exp(-q * T) * norm.pdf(d1) / (2 * sqrtT)
    if option_type == "Call":
        theta = (theta_term + q * S * np.exp(-q * T) * norm.cdf(d1)
                          - r * K * np.exp(-r * T) * norm.cdf(d2)) / 365
    else:
        theta = (theta_term - q * S * np.exp(-q * T) * norm.cdf(-d1)
                          + r * K * np.exp(-r * T) * norm.cdf(-d2)) / 365

    return price, delta, gamma, theta, vega, rho

# Configuration de la page
st.set_page_config(
    page_title="Calculateur de grecques",
    layout="wide"
)

st.title("Calculateur de Grecques : Δ, Γ, Θ, Vega, Rho")

# Sidebar pour les paramètres
with st.sidebar:
    st.header("Paramètres de l'option")
    option_type = st.selectbox("Type d'option", ["Call", "Put"])
    S     = st.number_input("Prix sous-jacent (S)", value=100.0, min_value=1e-6, format="%.4f")
    K     = st.number_input("Strike (K)", value=100.0, min_value=1e-6, format="%.4f")
    T     = st.number_input("Temps à échéance (années)", value=1.0, min_value=0.0, format="%.6f")
    r     = st.number_input("Taux sans risque r", value=0.05, format="%.4f")
    q     = st.number_input("Dividende continu q", value=0.02, format="%.4f")
    sigma = st.number_input("Volatilité σ", value=0.20, min_value=1e-6, format="%.4f")

# Calcul
price, delta, gamma, theta, vega, rho = black_scholes_greeks(S, K, T, r, sigma, q, option_type)

# Affichage des résultats en deux colonnes
st.header("Résultats")
col1, col2 = st.columns(2)

with col1:
    st.metric("Prix de l'option", f"{price:.4f} €")
    st.metric("Δ (Delta)",        f"{delta:.4f}")
    st.metric("Γ (Gamma)",        f"{gamma:.6f}")

with col2:
    st.metric("Θ (Theta)",        f"{theta:.6f} /j")
    st.metric("Vega",             f"{vega:.4f} /%σ")
    st.metric("Rho",              f"{rho:.4f} /%r")

# Explications
st.markdown("""
---
**Paramètres :**
- **S** : Prix actuel du sous-jacent  
- **K** : Prix d'exercice  
- **T** : Temps jusqu'à l'échéance (années)  
- **r** : Taux sans risque (continu, en décimal)  
- **q** : Taux de dividende continu (en décimal)  
- **σ** : Volatilité implicite (en décimal)  

**Grecques :**
- **Δ** (Delta) : sensibilité du prix de l’option à ΔS  
- **Γ** (Gamma) : sensibilité du Δ à ΔS  
- **Θ** (Theta) : perte de valeur **par jour**  
- **Vega** : sensibilité du prix à 1 pt de volatilité  
- **Rho** : sensibilité du prix à 1 pt du taux sans risque  
""")