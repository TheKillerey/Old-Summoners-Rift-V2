#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/sru_storekeepernorth/Animations/Skin0.bin"
    "DATA/Characters/sru_storekeepernorth/sru_storekeepernorth.bin"
}
entries: map[hash,embed] = {
    "Characters/sru_storekeepernorth/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_StoreKeeperNorth"
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Map11_ShopkeeperNorth_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_ShopkeeperNorth_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_ShopkeeperNorth_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/sru_storekeepernorth/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/sru_storekeepernorth/skins/base/SRU_storeKeeperNorth.skl"
            simpleSkin: string = "ASSETS/Characters/sru_storekeepernorth/skins/base/SRU_storeKeeperNorth.skn"
            texture: string = "ASSETS/Characters/sru_storekeepernorth/skins/base/SRU_storeKeeperNorth_TX_CM.dds"
            skinScale: f32 = 1.2
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
    }
}
