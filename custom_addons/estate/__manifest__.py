{
    "name": "Real Estate",
    "summary": "Test module",
    "category": "Real Estate",
    "sequence": -100,
    "version": "1.0.0",
    "depends": ["crm"],
    "data": [
        # security
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        # views
        "views/real_estate_views.xml",
        "views/real_estate_property_type_views.xml",
        "views/real_estate_property_offer_views.xml",
        "views/real_estate_property_tag_views.xml",
        "views/estate_menus.xml",
    ],
    "demo": [
        "demo/demo.xml"
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
