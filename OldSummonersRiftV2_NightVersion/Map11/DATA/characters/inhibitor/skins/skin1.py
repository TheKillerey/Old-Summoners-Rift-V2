#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Inhibitor/Inhibitor.bin"
    "DATA/Characters/Inhibitor/Animations/Skin2.bin"
    "DATA/Inhibitor_Skins_Skin0_Skins_Skin1_Skins_Skin12_Skins_Skin14_Skins_Skin15_Skins_Skin18_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin24_Skins_Skin25_Skins_Skin4_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/Inhibitor/Skins/Skin1" = SkinCharacterDataProperties {
        championSkinName: string = "Inhibitor_SR_Order_Red"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Inhibitor/Animations/Skin2"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Inhibitor/Skins/base/Inhibitor.skl"
            simpleSkin: string = "ASSETS/Characters/Inhibitor/Skins/base/Inhibitor.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/Inhibitor/Skins/base/Chaos_Inhibitor_diff.dds"
            selfIllumination: f32 = 0.5
            initialSubmeshToHide: string = "Destroyed"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Inhibitor/Skins/base/Inhibitor_destroyed_diff.dds"
                    submesh: string = "Destroyed"
                }
            }
        }
        armorMaterial: string = "Stone"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0x8eff98f7
                boneName: string = "joint2"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0x28a22e52
                boneName: string = "gem1"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0x28a22e52
                boneName: string = "gem2"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0x28a22e52
                boneName: string = "gem3"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0x28a22e52
                boneName: string = "gem4"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0x76c90cab
                boneName: string = "base2"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0x76c90cab
                boneName: string = "base3"
            }
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0x76c90cab
                boneName: string = "base4"
            }
        }
        particleOverride_DeathParticle: string = "Inhibitor_Explosion_Red.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/Inhibitor/HUD/Inhibitor_Red_Circle.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Inhibitor/HUD/Inhibitor_Red_Square.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 1
        }
        mResourceResolver: link = "Characters/Inhibitor/Skins/Skin1/Resources"
    }
    "Characters/Inhibitor/Skins/Skin1/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xf5e851af = "Characters/Inhibitor/Skins/Skin0/Particles/Order_Inhibit_Gem"
            0xfa6f453a = "Characters/Inhibitor/Skins/Skin0/Particles/Order_Inhibit_Crystal_Glow"
            0xe11a96a3 = "Characters/Inhibitor/Skins/Skin0/Particles/Order_Inhibit_Base_Glow"
            0x8eff98f7 = "Characters/Inhibitor/Skins/Skin0/Particles/Chaos_Inhibit_Gem"
            0x28a22e52 = "Characters/Inhibitor/Skins/Skin0/Particles/Chaos_Inhibit_Crystal_Glow"
            0x76c90cab = "Characters/Inhibitor/Skins/Skin0/Particles/Chaos_Inhibit_Base_Glow"
        }
    }
}
