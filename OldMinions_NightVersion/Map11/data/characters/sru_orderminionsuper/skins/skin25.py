#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_OrderMinionSuper/SRU_OrderMinionSuper.bin"
    "DATA/Characters/SRU_OrderMinionSuper/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_OrderMinionSuper/Skins/Skin25" = SkinCharacterDataProperties {
        championSkinName: string = "Order_Minion_Super_Bloom_Red"
        metaDataTags: string = "class:minion"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Global_Minions_OrderSuper_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderSuper_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Global_Minions_OrderSuper_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_OrderMinionSuper/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_OrderMinionSuper/skins/base/Blue_Minion_Superminion.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_OrderMinionSuper/skins/base/Blue_Minion_Superminion.skn"
            ReducedBoneSkinning: bool = true
            texture: string = "ASSETS/Characters/SRU_OrderMinionSuper/skins/base/blue_superminion_TX_CM_Red.dds"
            skinScale: f32 = 1.14999998
            selfIllumination: f32 = 0.600000024
        }
        armorMaterial: string = "Stone"
        mSpawnParticleName: string = "sru_minionSpawn_01.troy"
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionSuper/HUD/Redmechmelee_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_OrderMinionSuper/HUD/Redmechmelee_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 1
        }
    }
}
