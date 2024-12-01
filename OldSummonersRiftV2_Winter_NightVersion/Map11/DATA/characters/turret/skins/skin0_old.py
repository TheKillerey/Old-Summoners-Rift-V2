#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Turret/Turret.bin"
    "DATA/Characters/Turret/Animations/Skin0.bin"
    "DATA/Turret_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin13_Skins_Skin16_Skins_Skin17_Skins_Skin20_Skins_Skin22_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin4_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Turret_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin13_Skins_Skin16_Skins_Skin20_Skins_Skin22_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin4_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Turret_Skins_Skin10_Skins_Skin11_Skins_Skin14_Skins_Skin15_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin6_Skins_Skin7.bin"
}
entries: map[hash,embed] = {
    "Characters/Turret/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "Turret_SR_Order_Blue"
        emoteLoadout: hash = 0x9029a33d
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Turret/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Turret/Skins/base/Order_Turret.skl"
            simpleSkin: string = "ASSETS/Characters/Turret/Skins/base/Order_Turret.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/Turret/Skins/base/Turret_TX_CM.dds"
            skinScale: f32 = 1.10000002
            selfIllumination: f32 = 0.5
            brushAlphaOverride: f32 = 1
        }
        armorMaterial: string = "Stone"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Order_Turret_Crystal"
                boneName: string = "joint2"
            }
        }
        iconCircle: option[string] = {
            "ASSETS/Characters/Turret/HUD/Turret_Blue_Circle.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Turret/HUD/Turret_Blue_Square.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 1
        }
        mResourceResolver: link = "Characters/Turret/Skins/Skin0/Resources"
    }
    "Characters/Turret/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xec90fddd = "Characters/Turret/Skins/Skin0/Particles/SRU_Order_Turret_BA"
            0xf118ff29 = "Characters/Turret/Skins/Skin0/Particles/SRU_Order_Turret_BA_Champ"
            0x9ef2bde5 = "Characters/Turret/Skins/Skin0/Particles/SRU_Order_Turret_BA_Tar"
            0x127fbf81 = "Characters/Turret/Skins/Skin0/Particles/SRU_Order_Turret_BA_Tar_Champ"
            0xe8e6cb63 = "Maps/Characters/Turret/Skins/SR/Particles/Order_Turret_Crystal"
        }
    }
}
