import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config

class loaStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}