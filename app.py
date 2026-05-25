import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="HAL Tejas Sonic Boom Simulator", layout="wide", page_icon="✈️")

st.title("✈️ HAL Tejas Sonic Boom Simulator")
st.markdown("### Real-time supersonic flight physics simulator")

st.sidebar.header("Flight Parameters")
mach = st.sidebar.slider("Mach Number", 0.1, 3.0, 0.8, 0.01)
altitude = st.sidebar.slider("Altitude (m)", 0, 20000, 5000, 100)

temp = 288.15 - 0.0065 * altitude
speed_of_sound = np.sqrt(1.4 * 287 * temp)
aircraft_speed = mach * speed_of_sound

if mach < 0.8:
    regime = "Subsonic"
elif mach < 1.0:
    regime = "Transonic"
else:
    regime = "Supersonic - SONIC BOOM"

st.sidebar.markdown(f"### Flight Regime: {regime}")
st.sidebar.metric("Speed of Sound at Altitude", f"{speed_of_sound:.1f} m/s")
st.sidebar.metric("Aircraft Speed", f"{aircraft_speed:.1f} m/s")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Shockwave Cone Visualisation")
    if mach >= 1.0:
        half_angle = np.degrees(np.arcsin(1 / mach))
        theta = np.radians(half_angle)
        x = np.linspace(0, 10, 100)
        y_upper = np.tan(theta) * x
        y_lower = -np.tan(theta) * x

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=x, y=y_upper,
            mode='lines',
            line=dict(color='red', width=3),
            name='Shockwave'
        ))
        fig1.add_trace(go.Scatter(
            x=x, y=y_lower,
            mode='lines',
            line=dict(color='red', width=3),
            showlegend=False
        ))
        fig1.add_trace(go.Scatter(
            x=[0], y=[0],
            mode='markers+text',
            marker=dict(size=15, color='blue', symbol='triangle-right'),
            text=['HAL Tejas'],
            textposition='top center'
        ))
        fig1.update_layout(
            title=f"Mach Cone — Half Angle: {half_angle:.1f}°",
            xaxis_title="Distance",
            yaxis_title="Width",
            template="plotly_dark"
        )
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("No shockwave at subsonic speeds. Increase Mach to 1.0+ to see the cone.")

with col2:
    st.subheader("Pressure Wave Visualisation")
    x_wave = np.linspace(-10, 10, 500)
    if mach >= 1.0:
        pressure = np.where(
            np.abs(x_wave) < 0.5,
            3.0,
            1.0 + 0.3 * np.exp(-0.5 * x_wave**2) * np.sin(5 * x_wave)
        )
    else:
        pressure = 1.0 + 0.3 * np.exp(-0.5 * (x_wave / mach)**2) * np.cos(3 * x_wave)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=x_wave, y=pressure,
        mode='lines',
        line=dict(color='cyan', width=2)
    ))
    fig2.update_layout(
        title="Pressure Distribution Around Aircraft",
        xaxis_title="Position",
        yaxis_title="Relative Pressure",
        template="plotly_dark"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Flight Data")
col3, col4, col5, col6 = st.columns(4)
col3.metric("Mach Number", f"{mach:.2f}")
col4.metric("Altitude", f"{altitude:,} m")
col5.metric("Temperature at Altitude", f"{temp:.1f} K")
col6.metric("Aircraft Speed", f"{aircraft_speed:.0f} m/s")

if mach >= 1.0:
    half_angle = np.degrees(np.arcsin(1 / mach))
    st.error(f"SONIC BOOM GENERATED — Shockwave half-angle: {half_angle:.1f}°")
elif mach >= 0.8:
    st.warning("Approaching transonic regime — compressibility effects increasing")
else:
    st.success("Subsonic flight — normal aerodynamic conditions")
