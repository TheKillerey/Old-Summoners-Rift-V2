#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/PreSeason_Turret_Shield_Skins_Skin0_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin3_Skins_Skin4_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/PreSeason_Turret_Shield/PreSeason_Turret_Shield.bin"
    "DATA/Characters/PreSeason_Turret_Shield/Animations/Skin0.bin"
    "DATA/PreSeason_Turret_Shield_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/PreSeason_Turret_Shield/Skins/Skin4" = SkinCharacterDataProperties {
        championSkinName: string = "Milkshake_Blue"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/PreSeason_Turret_Shield/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin04/Order_Blue.Milkshake_Env.skl"
            simpleSkin: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin04/Order_Blue.Milkshake_Env.skn"
            texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin04/PreSeason_Turret_Shield_Skin04_Order_Blue_TX_CM.Milkshake_Env.tex"
            skinScale: f32 = 0
            selfIllumination: f32 = 0.8
            brushAlphaOverride: f32 = 1
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Tower_Palisades_Order_Broken_Part1_Mat Tower_Palisades_Order_Broken_Part2_Mat Tower_Palisades_Order_Broken_Part3_Mat Tower_Palisades_Order_Broken_Part5_Mat Tower_Palisades_Order_Broken_Part4_Mat"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin04/PreSeason_Turret_Shield_Skin04_Order_Blue_Dark_Gem_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Order_Broken_Part1_Mat"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin04/PreSeason_Turret_Shield_Skin04_Order_Blue_Dark_Gem_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Order_Broken_Part2_Mat"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin04/PreSeason_Turret_Shield_Skin04_Order_Blue_Dark_Gem_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Order_Broken_Part3_Mat"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin04/PreSeason_Turret_Shield_Skin04_Order_Blue_Dark_Gem_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Order_Broken_Part4_Mat"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/PreSeason_Turret_Shield/Skins/Skin04/PreSeason_Turret_Shield_Skin04_Order_Blue_Dark_Gem_TX_CM.Milkshake_Env.tex"
                    submesh: string = "Tower_Palisades_Order_Broken_Part5_Mat"
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
        mResourceResolver: link = "Characters/PreSeason_Turret_Shield/Skins/Skin4/Resources"
    }
    "Characters/PreSeason_Turret_Shield/Skins/Skin4/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "PreSeason_Turret_Shield_Break_1" = "Characters/PreSeason_Turret_Shield/Skins/Skin0/Particles/PreSeason_Turret_Shield_Base_Break_1"
            "PreSeason_Turret_Shield_Ground_Dust" = "Characters/PreSeason_Turret_Shield/Skins/Skin0/Particles/PreSeason_Turret_Shield_Base_Ground_Dust"
            "PreSeason_Turret_Shield_Spawn" = "Characters/PreSeason_Turret_Shield/Skins/Skin0/Particles/PreSeason_Turret_Shield_Base_Spawn"
            "PreSeason_Turret_Shield_Crystal_Burst" = "Characters/PreSeason_Turret_Shield/Skins/Skin0/Particles/PreSeason_Turret_Shield_Base_Crystal_Burst"
        }
    }
}
