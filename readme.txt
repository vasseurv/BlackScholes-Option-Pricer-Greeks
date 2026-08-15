GREEKS CALCULATOR + BLACK-SCHOLES OPTION PRICER
================================================

This Streamlit application calculates the price of a European option and the
following Greeks using the Black-Scholes model with continuous dividends:

- Delta (Δ)
- Gamma (Γ)
- Theta (Θ), expressed per day
- Vega, for a one percentage-point change in volatility
- Rho, for a one percentage-point change in the risk-free rate


REQUIREMENTS
------------

Python 3.9 or later is required.

The application uses the following libraries:

    streamlit
    numpy
    scipy


INSTALLATION
------------

From a terminal, move to the project directory.

Creating a virtual environment is recommended:

    python3 -m venv .venv
    source .venv/bin/activate

Then install the dependencies:

    pip install streamlit numpy scipy


RUN THE APPLICATION
-------------------

In the same terminal, run:

    streamlit run app.py

Streamlit should open the application in your browser. If it does not, open the
address displayed in the terminal, usually http://localhost:8501.

To stop the application, return to the terminal and press Ctrl+C.


USAGE
-----

Set the parameters in the left sidebar.

Results update automatically whenever a parameter is changed. The purpose of
the application is to observe how the Greeks vary as the option parameters are
modified.


NOTES
-----

- The model applies to European options.
- At maturity (T = 0), the application returns the option's intrinsic value;
  Greeks other than delta are shown as zero.
