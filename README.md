# Meeting Summarizer

A web based Meeting Summarizer that converts meeting audio into a text transcript and generates an AI powered meeting summary.

## Overview

The Meeting Summarizer accepts an audio recording through a web interface. The uploaded audio is processed by the backend to generate a transcript using speech to text processing. The transcript is then passed to a Gemini based summarization module to generate a concise meeting summary.

The application provides both the original transcript and the generated summary through a simple web interface.

## Features

• Upload meeting audio files

• Speech to text transcription

• AI powered meeting summarization

• Key decisions extraction

• Action item identification

• Responsible person identification when mentioned in the transcript

• Web based user interface

• FastAPI backend

## System Workflow

```text
Meeting Audio
      |
      v
Frontend Upload
      |
      v
FastAPI Backend
      |
      v
Speech to Text
      |
      v
Transcript
      |
      v
Gemini AI
      |
      v
Meeting Summary
      |
      v
Frontend Display
