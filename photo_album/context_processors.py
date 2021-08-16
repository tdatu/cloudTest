import cloudinary
def consts(request):
    return dict(
        ICON_EFFECTS = dict(
            format="png",
            type="facebook",
            transformation=[
                dict(height=95, width=95, crop="thumb", gravity="face", effect="sepia", radius=20),
                dict(angle=10),
            ]
        ),
        THUMBNAIL = {
            "class": "thumbnail inline", "format": "jpg", "crop": "fill", "height": 150, "width": 150,
        },
        THUMBNAIL_OVERLAY = dict(
            dict(transformation=[
                dict(height=150,width=150,crop="fill"),
                dict(overlay="sample_watermark",crop="scale",width=40,gravity="south_east",x=5,y=10),
                ])
            ),
        THUMBNAIL_CONTRAST= dict(
            dict(transformation=[
                dict(effect="contrast:50"),
                dict(crop="fill", height=150, width=150),
                ])
            ),
        CLOUDINARY_CLOUD_NAME = cloudinary.config().cloud_name
    )
