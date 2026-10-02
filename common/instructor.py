"""Instructor-only controls for class activity pages.

Clearing shared class submissions is limited to whoever has the instructor key, so
public visitors cannot wipe a class's data. The key comes from the
CONSERVATION_INSTRUCTOR_KEY environment variable (set in this app's .env file).
If the variable is unset, the clear controls are turned off.
"""
import hmac
import os

import streamlit as st


def instructor_clear_button(label: str, key: str) -> bool:
    """Render an 'Instructor tools' expander; return True when the instructor clicks clear."""
    secret = os.environ.get("CONSERVATION_INSTRUCTOR_KEY", "")
    with st.expander("Instructor tools"):
        if not secret:
            st.caption("Instructor tools are turned off on this site.")
            return False
        entered = st.text_input("Instructor key", type="password", key=f"{key}_instructor_key")
        if entered and not hmac.compare_digest(entered, secret):
            st.error("Incorrect instructor key.")
            return False
        return st.button(label, key=f"{key}_clear", disabled=not entered)
