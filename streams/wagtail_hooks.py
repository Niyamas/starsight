"""
Addendums to Wagtail's rich text editor.
See: https://www.youtube.com/watch?v=A4M0MEtE_H0&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=29&ab_channel=CodingForEverybody
"""

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler
)
from wagtail.core import hooks


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