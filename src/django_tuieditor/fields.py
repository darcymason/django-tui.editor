from django import forms

from .widgets import MarkdownEditorWidget, MarkdownViewerWidget


class MarkdownFormField(forms.CharField):
    widget = MarkdownEditorWidget

class MarkdownViewerFormField(forms.CharField):
    widget = MarkdownViewerWidget