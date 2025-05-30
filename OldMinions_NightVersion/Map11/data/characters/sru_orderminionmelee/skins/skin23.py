#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_OrderMinionMelee/Animations/Skin23.bin"
    "DATA/Characters/SRU_OrderMinionMelee/SRU_OrderMinionMelee.bin"
}
entries: map[hash,embed] = {
    0xd4ad7d23 = SkinCharacterDataProperties {
        championSkinName: string = "Order_Minion_Melee_SRS_Red"
        metaDataTags: string = "class:minion"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Global_Minions_OrderMelee_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderMelee_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderMelee_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = 0x01d6b874
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_OrderMinionMelee/Skins/Base/Order_Minion_Melee.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_OrderMinionMelee/Skins/Base/Order_Minion_Melee.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRU_OrderMinionMelee/Skins/Base/OrderMinion_Melee_TX_CM_Red.dds"
            skinScale: f32 = 0.939999998
            selfIllumination: f32 = 0.600000024
        }
        armorMaterial: string = "Flesh"
        mSpawnParticleName: string = "sru_minionSpawn_01.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionMelee/HUD/RedMelee_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionMelee/HUD/RedMelee_Square.tex"
        }
    }
}
