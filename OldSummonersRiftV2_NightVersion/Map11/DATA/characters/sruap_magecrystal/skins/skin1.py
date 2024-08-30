#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRUAP_MageCrystal/SRUAP_MageCrystal.bin"
    "DATA/Characters/SRUAP_MageCrystal/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRUAP_MageCrystal/Skins/Skin1" = SkinCharacterDataProperties {
        championSkinName: string = "MageCrystal_BASE_Blue"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRUAP_MageCrystal/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRUAP_MageCrystal/Skins/Base/SRUAP_MageCrystal.skl"
            simpleSkin: string = "ASSETS/Characters/SRUAP_MageCrystal/Skins/Base/SRUAP_MageCrystal.skn"
            ReducedBoneSkinning: bool = true
            skinScale: f32 = 2
            texture: string = "ASSETS/Characters/SRUAP_MageCrystal/Skins/Base/SRUAP_MageCrystal_TX_CM_blue.dds"
            selfIllumination: f32 = 0.699999988
        }
        armorMaterial: string = "Stone"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRUAP_MageCrystal/HUD/Turret_Blue_Circle.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRUAP_MageCrystal/HUD/Turret_Blue_Square.dds"
        }
    }
}
