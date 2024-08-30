#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/sru_dragon_earth/sru_dragon_earth.bin"
    "DATA/Characters/sru_dragon_earth/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/sru_dragon_earth/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Dragon_Earth"
        metaDataTags: string = "monstertype:dragon"
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "SRU_Dragon_Mountain"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Map11_Dragons_Mountain_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_Mountain_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_Mountain_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_SRU_Dragon_Mountain_Attack_OnCast"
                        "Play_sfx_SRU_Dragon_Mountain_Attack_OnHitLocation"
                        "Play_sfx_SRU_Dragon_Mountain_Attack_OnMissileLaunch"
                        "Play_vo_SRU_Dragon_Mountain_Attack_OnCast"
                    }
                }
                BankUnit {
                    name: string = "NPC_Map11_Dragons_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_SRU_Dragon_ag2al_buffactive"
                        "Play_sfx_SRU_Dragon_aggro1_buffactive"
                        "Play_sfx_SRU_Dragon_aggro3_buffactive"
                        "Play_sfx_SRU_Dragon_aggro4_buffactive"
                        "Play_sfx_SRU_Dragon_aggro5_buffactive"
                        "Play_sfx_SRU_Dragon_aggro6_buffactive"
                        "Play_sfx_SRU_Dragon_aggro7_buffactive"
                        "Play_sfx_SRU_Dragon_al2ag_buffactive"
                        "Play_sfx_SRU_Dragon_al2n_buffactive"
                        "Play_sfx_SRU_Dragon_alert2_buffactive"
                        "Play_sfx_SRU_Dragon_alert3_buffactive"
                        "Play_sfx_SRU_Dragon_death_cast"
                        "Play_sfx_SRU_Dragon_death_reverb"
                        "Play_sfx_SRU_Dragon_DragonFireball2_OnMissileCast"
                        "Play_sfx_SRU_Dragon_DragonFireball2_OnMissileLaunch"
                        "Play_sfx_SRU_Dragon_DragonFireball_hit"
                        "Play_sfx_SRU_Dragon_DragonFireball_OnCast"
                        "Play_sfx_SRU_Dragon_DragonTakeOff_cast"
                        "Play_sfx_SRU_Dragon_hover_buffactive"
                        "Play_sfx_SRU_Dragon_landing_buffactive"
                        "Play_sfx_SRU_Dragon_n2al_buffactive"
                        "Play_sfx_SRU_Dragon_spawn_cast"
                        "Play_sfx_SRU_Dragon_spawn_cast_vox"
                        "Stop_sfx_SRU_Dragon_ag2al_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro1_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro3_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro4_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro5_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro6_buffactive"
                        "Stop_sfx_SRU_Dragon_aggro7_buffactive"
                        "Stop_sfx_SRU_Dragon_al2ag_buffactive"
                        "Stop_sfx_SRU_Dragon_al2n_buffactive"
                        "Stop_sfx_SRU_Dragon_alert2_buffactive"
                        "Stop_sfx_SRU_Dragon_alert3_buffactive"
                        "Stop_sfx_SRU_Dragon_death_cast"
                        "Stop_sfx_SRU_Dragon_death_vox_cast"
                        "Stop_sfx_SRU_Dragon_DragonFireball2_OnMissileCast"
                        "Stop_sfx_SRU_Dragon_DragonFireball2_OnMissileLaunch"
                        "Stop_sfx_SRU_Dragon_DragonFireball_OnCast"
                        "Stop_sfx_SRU_Dragon_hover_buffactive"
                        "Stop_sfx_SRU_Dragon_landing_buffactive"
                        "Stop_sfx_SRU_Dragon_n2al_buffactive"
                        "Stop_sfx_SRU_Dragon_spawn_cast_vox"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/sru_dragon_earth/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/sru_dragon_earth/Skins/Base/SRU_Dragon_Earth.skl"
            simpleSkin: string = "ASSETS/Characters/sru_dragon_earth/Skins/Base/SRU_Dragon_Earth.skn"
            texture: string = "ASSETS/Characters/sru_dragon_earth/Skins/Base/SRU_Dragon_Earth_TX_CM.dds"
            skinScale: f32 = 3
            selfIllumination: f32 = 0.699999988
            brushAlphaOverride: f32 = 1
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Flesh"
        iconCircle: option[string] = {
            "ASSETS/Characters/sru_dragon_earth/HUD/Dragon_Circle_Earth.dds"
        }
        iconCircleScale: option[f32] = {
            1.20000005
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/sru_dragon_earth/HUD/Dragon_Square_Earth.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1000
            attachToBone: string = "Buffbone_Cstm_Healthbar"
            unitHealthBarStyle: u8 = 5
        }
        mResourceResolver: link = "Characters/sru_dragon_earth/Skins/Skin0/Resources"
    }
    "Characters/sru_dragon_earth/Skins/Skin0/Particles/sru_dragon_earth_Base_BA_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Flash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                falloffTexture: string = ""
                particleColorTexture: string = ""
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.854902029, 0.619607985, 0.500007987 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.854902029, 0.619607985, 0.500007987 }
                            { 1, 0.854902029, 0.619607985, 0 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -2
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 300, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_earth/Skins/Base/Particles/sru_dragon_earth_BA_Jinx_Muzzle_Flash.dds"
                numFrames: u16 = 4
                startFrame: u16 = 1
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.320000023
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "shockwaveContrast"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                falloffTexture: string = ""
                particleColorTexture: string = ""
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.254902005, 0.156863004, 0.113724999, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.254902005, 0.156863004, 0.113724999, 0.600000024 }
                            { 0.254902005, 0.156863004, 0.113724999, 0.600000024 }
                            { 0.254902005, 0.156863004, 0.113724999, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 180, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1.20000005, 1.20000005, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_earth/Skins/Base/Particles/sru_dragon_earth_Base_BA_Mis_AOE_Impact_Darkener.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Stone_Bits"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 1500, 250 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 250, 1500, 250 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -6000, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -6000, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 0, 50 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 50, 0, 50 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_earth/Skins/Base/Particles/sru_dragon_earth_Base_X_Small_Stone.scb"
                    }
                }
                falloffTexture: string = ""
                particleColorTexture: string = ""
                blendMode: u8 = 3
                isRandomStartFrame: flag = true
                doesCastShadow: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 80 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 80, 80 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1.5, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 1.5, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_earth/Skins/Base/Particles/sru_dragon_earth_Base_X_Small_Stone.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 2, 3 }
            }
        }
        particleName: string = "sru_dragon_earth_Base_BA_Tar"
        particlePath: string = "Characters/sru_dragon_earth/Skins/Skin0/Particles/sru_dragon_earth_Base_BA_Tar"
        flags: u16 = 198
    }
    "Characters/sru_dragon_earth/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0x095a23c0 = "Characters/sru_dragon_earth/Skins/Skin0/Particles/sru_dragon_earth_Base_BA_Tar"
        }
    }
}
