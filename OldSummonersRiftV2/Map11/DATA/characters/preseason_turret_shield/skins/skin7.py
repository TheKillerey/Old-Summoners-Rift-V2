#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/PreSeason_Turret_Shield/PreSeason_Turret_Shield.bin"
    "DATA/PreSeason_Turret_Shield_Skins_Skin1_Skins_Skin15_Skins_Skin2_Skins_Skin5_Skins_Skin6_Skins_Skin7.bin"
    "DATA/Characters/PreSeason_Turret_Shield/Animations/Skin2.bin"
    "DATA/PreSeason_Turret_Shield_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/PreSeason_Turret_Shield/Skins/Skin7" = SkinCharacterDataProperties {
        championSkinName: string = "Milkshake_Red"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/PreSeason_Turret_Shield/Animations/Skin2"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin07/PreSeason_Turret_Shield.Milkshake_Env.skl"
            simpleSkin: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin07/PreSeason_Turret_Shield.Milkshake_Env.skn"
            texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin07/PreSeason_Turret_Shield_Skin07_Chaos_Red_TX_CM.Milkshake_Env.tex"
            skinScale: f32 = 0
            selfIllumination: f32 = 0.8
            brushAlphaOverride: f32 = 1
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Tower_Palisades_Chaos_Broken_Part1_Mat Tower_Palisades_Chaos_Broken_Part2_Mat Tower_Palisades_Chaos_Broken_Part3_Mat Tower_Palisades_Chaos_Broken_Part4_Mat Tower_Palisades_Chaos_Broken_Part5_Mat"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin07/PreSeason_Turret_Shield_Skin07_Chaos_Red_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Chaos_Broken_Part1_Mat"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin07/PreSeason_Turret_Shield_Skin07_Chaos_Red_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Chaos_Broken_Part2_Mat"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin07/PreSeason_Turret_Shield_Skin07_Chaos_Red_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Chaos_Broken_Part3_Mat"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin07/PreSeason_Turret_Shield_Skin07_Chaos_Red_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Chaos_Broken_Part4_Mat"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin07/PreSeason_Turret_Shield_Skin07_Chaos_Red_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Chaos_Broken_Part5_Mat"
                }
            }
        }
        armorMaterial: string = "Wood"
        iconCircle: option[string] = {
            "ASSETS/Characters/PreSeason_Turret_Shield/HUD/PreSeason_Turret_Shield_Circle_0.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/PreSeason_Turret_Shield/HUD/PreSeason_Turret_Shield_Square_0.tex"
        }
        emoteBuffbone: string = ""
        godrayFXbone: string = ""
        mResourceResolver: link = "Characters/PreSeason_Turret_Shield/Skins/Skin7/Resources"
    }
    "Characters/PreSeason_Turret_Shield/Skins/Skin7/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "PreSeason_Turret_Shield_Break_1" = "Characters/PreSeason_Turret_Shield/Skins/Skin0/Particles/PreSeason_Turret_Shield_Base_Break_1"
            "PreSeason_Turret_Shield_Ground_Dust" = "Characters/PreSeason_Turret_Shield/Skins/Skin0/Particles/PreSeason_Turret_Shield_Base_Ground_Dust"
            "PreSeason_Turret_Shield_Spawn" = "Characters/PreSeason_Turret_Shield/Skins/Skin0/Particles/PreSeason_Turret_Shield_Base_Spawn"
            "PreSeason_Turret_Shield_Crystal_Burst" = "Characters/PreSeason_Turret_Shield/Skins/Skin2/Particles/PreSeason_Turret_Shield_Skin02_Crystal_Burst"
        }
    }
}
