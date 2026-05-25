#  HAL Tejas Sonic Boom Simulator

A real time interactive supersonic flight physics simulator built for the HAL Tejas fighter jet.

## What it does
- Simulates the four forces of flight in real time
- Visualises shockwave cone formation when the aircraft breaks the sound barrier
- Models pressure wave distribution around the aircraft
- Calculates speed of sound at any altitude using real atmospheric data
- Detects subsonic, transonic and supersonic flight regimes

## Physics behind it
- International Standard Atmosphere (ISA) model for temperature and speed of sound at altitude
- Mach cone half angle calculated using: θ = arcsin(1/M)
- Real atmospheric lapse rate of 6.5K per 1000m altitude gain
- Pressure wave modelling based on compressibility effects

## Tech Stack
- Python
- Streamlit
- Plotly
- NumPy

## How to run
pip install streamlit plotly numpy pandas
python -m streamlit run app.py

## About
Built by Atharv Shukla, Class 12, Amity International School Sector 46 Gurgaon.
Part of a self directed aerospace engineering project portfolio.
Inspired by HAL's Tejas Mk1A supersonic fighter jet program.
