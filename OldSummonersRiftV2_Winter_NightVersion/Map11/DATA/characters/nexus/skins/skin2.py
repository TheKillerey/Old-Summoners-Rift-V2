#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Nexus/Nexus.bin"
    "DATA/Characters/Nexus/Animations/Skin0.bin"
    "DATA/Nexus_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin13_Skins_Skin16_Skins_Skin17_Skins_Skin4_Skins_Skin5_Skins_Skin8.bin"
}
entries: map[hash,embed] = {
    "Characters/Nexus/Skins/Skin2" = SkinCharacterDataProperties {
        championSkinName: string = "Nexus_SR_Chaos_Blue"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Nexus/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Nexus/Skins/Base/Nexus.skl"
            simpleSkin: string = "ASSETS/Characters/Nexus/Skins/Base/Nexus.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/Nexus/Skins/Base/Nexus_diff.dds"
            selfIllumination: f32 = 0.5
            initialSubmeshToHide: string = "Destroyed"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Nexus/Skins/Base/Nexus_Destroyed_diff.dds"
                    submesh: string = "Destroyed"
                }
            }
        }
        armorMaterial: string = "Stone"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus"
                boneName: string = "center"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow"
                boneName: string = "gnome1"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow"
                boneName: string = "gnome2"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow"
                boneName: string = "gnome3"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow"
                boneName: string = "gnome4"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow"
                boneName: string = "gnome5"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow"
                boneName: string = "gnome6"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Base_Glow"
                boneName: string = "base3"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Base_Glow"
                boneName: string = "base4"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Base_Glow"
                boneName: string = "base5"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Base_Glow"
                boneName: string = "base6"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow_on"
                boneName: string = "gnome1"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow_on"
                boneName: string = "gnome2"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow_on"
                boneName: string = "gnome3"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow_on"
                boneName: string = "gnome4"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow_on"
                boneName: string = "gnome5"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Crystal_Glow_on"
                boneName: string = "gnome6"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Base_Glow_on"
                boneName: string = "base3"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Base_Glow_on"
                boneName: string = "base4"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Base_Glow_on"
                boneName: string = "base5"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "Order_Nexus_Base_Glow_on"
                boneName: string = "base6"
            }
        }
        particleOverride_DeathParticle: string = "Nexus_Explosion_Blue.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/Nexus/HUD/Nexus_Blue_Circle.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Nexus/HUD/Nexus_Red_Square.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 1
        }
        mResourceResolver: link = "Characters/Nexus/Skins/Root/Resources"
    }
}
