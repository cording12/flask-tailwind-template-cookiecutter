"""Compile static assets
Explanation of using assets/bundles in app factory here:
https://stackoverflow.com/questions/59740924/flask-assets-how-to-keep-an-specific-apps-static-js-files-from-being-used-by
"""
from flask import current_app as app
from flask_assets import Bundle


def compile_assets(assets):
    """Create stylesheet bundles."""
    assets.auto_build = True
    assets.debug = False

    common_style_bundle = Bundle(
        "src/css/*.css",
        filters="cssmin",
        output="dist/css/tailwind-min.css",
        extra={"rel": "stylesheet/css"},
    )

    common_js_bundle = Bundle(
        "src/js/*.js",
        filters="jsmin",
        output="dist/js/main.min.js",
        extra={"rel": "stylesheet/less"},
    )

    lib_js_bundle = Bundle(
        "src/js/lib/*.js",
        filters="jsmin",
        output="dist/js/lib/lib.min.js",
    )

    home_style_bundle = Bundle(
        "home_bp/css/*.css",
        filters="cssmin",
        output="dist/css/home.min.css",
        extra={"rel": "stylesheet/css"},
    )

    home_js_bundle = Bundle(
        "home_bp/js/*.js",
        filters="jsmin",
        output="dist/js/home.min.js",
    )

    assets.register("common_style_bundle", common_style_bundle)
    assets.register("home_style_bundle", home_style_bundle)

    assets.register("common_js_bundle", common_js_bundle)
    assets.register("home_js_bundle", home_js_bundle)

    assets.register("lib_js_bundle", lib_js_bundle)

    if app.config["FLASK_ENV"] == "development":
        common_style_bundle.build()
        home_style_bundle.build()
        common_js_bundle.build()
        home_js_bundle.build()
        lib_js_bundle.build()

    return assets
