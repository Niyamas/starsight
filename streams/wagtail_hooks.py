"""
Addendums to Wagtail's rich text editor.
See: https://www.youtube.com/watch?v=A4M0MEtE_H0&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=29&ab_channel=CodingForEverybody
"""

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler,
    LinkElementHandler
)
from wagtail.core import hooks
from wagtail.core.rich_text import LinkHandler
from django.utils.html import escape


@hooks.register('register_rich_text_features')
def register_code_styling(features):
    """Add the <code> to the richtext editor."""

    feature_name = 'code'
    type_ = 'CODE'
    tag = 'code'

    control = {
        'type': type_,
        'label': '</>',
        'description': 'Code'
    }

    features.register_editor_plugin('draftail', feature_name, draftail_features.InlineStyleFeature(control))

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': { 'style_map': {type_: {'element': tag}} }
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    # This will register this feature with all richtext editors by default.
    features.default_features.append(feature_name)


@hooks.register('register_rich_text_features')
def register_centertext_feature(features):
    """Add centered text in the richtext editor."""

    feature_name = 'center'
    type_ = 'CENTERTEXT'
    tag = 'div'

    control = {
        'type': type_,
        'label': 'Center',
        'description': 'Center Text',
        'style': {
            'display': 'block',
            'text-align': 'center'
        }
    }

    features.register_editor_plugin('draftail', feature_name, draftail_features.InlineStyleFeature(control))

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'd-block text-center'
                    }
                }
            }
        }
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    # This will register this feature with all richtext editors by default.
    features.default_features.append(feature_name)


# External links generated by rich texts will now open in a new tab
# See: https://stackoverflow.com/questions/33300941/making-external-links-open-in-a-new-window-in-wagtail
class NewWindowExternalLinkHandler(LinkHandler):
    # This specifies to do this override for external links only.
    # Other identifiers are available for other types of links.
    identifier = 'external'

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs["href"]
        # Let's add the target attr, and also rel="noopener" + noreferrer fallback.
        # See https://github.com/whatwg/html/issues/4078.
        return '<a href="%s" target="_blank" rel="noopener noreferrer">' % escape(href)


@hooks.register('register_rich_text_features')
def register_external_link(features):
    features.register_link_type(NewWindowExternalLinkHandler)