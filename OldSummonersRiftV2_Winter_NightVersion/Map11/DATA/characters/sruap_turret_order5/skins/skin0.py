#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRUAP_Turret_Order5/Animations/Skin0.bin"
    "DATA/Characters/SRUAP_Turret_Order5/SRUAP_Turret_Order5.bin"
}
entries: map[hash,embed] = {
    "Characters/SRUAP_Turret_Order5/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRUAPTurretOrder5"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRUAP_Turret_Order5/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRUAP_Turret_Order5/skins/base/SRUAP_Turret_Order5.skl"
            simpleSkin: string = "ASSETS/Characters/SRUAP_Turret_Order5/skins/base/SRUAP_Turret_Order5.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRUAP_Turret_Order5/skins/base/SRUAP_Turret_Pali5.dds"
            skinScale: f32 = 0.9
            selfIllumination: f32 = 0.5
            brushAlphaOverride: f32 = 1
        }
        armorMaterial: string = "Stone"
        iconCircle: option[string] = {
            "ASSETS/Characters/Turret/HUD/Turret_Blue_Circle.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Turret/HUD/Turret_Blue_Square.dds"
        }
    }
}
