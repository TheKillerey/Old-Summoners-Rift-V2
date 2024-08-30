#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_Blue/Animations/Skin4.bin"
    "DATA/Characters/SRU_Blue/SRU_Blue.bin"
    "DATA/SRU_Blue_Skins_Skin0_Skins_Skin3_Skins_Skin4.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_Blue/Skins/Skin4" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Blue_Baron"
        skinUpgradeData: embed = skinUpgradeData {
            mGearSkinUpgrades: list[link] = {
                0x632e5ade
                0xc7020d4f
            }
        }
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Map11_Blue_Base_Voidborn_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Blue_Base_Voidborn_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Blue_Base_Voidborn_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_SRU_Blue_Base_Voidborn_a2n_buffactivate"
                        "Play_sfx_SRU_Blue_Base_Voidborn_aggro1"
                        "Play_sfx_SRU_Blue_Base_Voidborn_aggro2"
                        "Play_sfx_SRU_Blue_Base_Voidborn_aggro3"
                        "Play_sfx_SRU_Blue_Base_Voidborn_BasicAttack2_cast"
                        "Play_sfx_SRU_Blue_Base_Voidborn_BasicAttack2_hit"
                        "Play_sfx_SRU_Blue_Base_Voidborn_BasicAttack3_cast"
                        "Play_sfx_SRU_Blue_Base_Voidborn_BasicAttack3_hit"
                        "Play_sfx_SRU_Blue_Base_Voidborn_BasicAttack_cast"
                        "Play_sfx_SRU_Blue_Base_Voidborn_BasicAttack_hit"
                        "Play_sfx_SRU_Blue_Base_Voidborn_death_cast"
                        "Play_sfx_SRU_Blue_Base_Voidborn_n2a_buffactivate"
                        "Play_sfx_SRU_Blue_Base_Voidborn_spawn_cast"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_a2n_buffactivate"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_aggro1"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_aggro2"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_aggro3"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_BasicAttack2_cast"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_BasicAttack2_hit"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_BasicAttack3_cast"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_BasicAttack3_hit"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_BasicAttack_cast"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_BasicAttack_hit"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_death_cast"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_n2a_buffactivate"
                        "Stop_sfx_SRU_Blue_Base_Voidborn_spawn_cast"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = 0x0220f273
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Skin04.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Skin04.skn"
            texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/SRU_Blue_Skin04_TX_CM.dds"
            skinScale: f32 = 1.37
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Normal"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/SRU_Blue_Golem_V2.dds"
                    submesh: string = "Normal"
                }
            }
        }
        armorMaterial: string = "Stone"
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "neutralmonster_buf_blue_defense_big.troy"
                boneName: string = "Root"
            }
        }
        iconCircle: option[string] = {
            "ASSETS/Characters/SRU_Blue/HUD/BlueSentinel_Circle.dds"
        }
        iconCircleScale: option[f32] = {
            1.20000005
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/SRU_Blue/HUD/BlueSentinel_Square.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1000
            unitHealthBarStyle: u8 = 5
        }
        mResourceResolver: link = "Characters/SRU_Blue/Skins/Skin4/Resources"
    }
    "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_idle" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 13
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
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
                emitterName: string = "Bluebuff_whitecenter"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 28 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.227420464, 0.880765975, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.699999988, 0.699999988, 0.699999988, 1 }
                            { 0.400000006, 0.400000006, 0.400000006, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 2
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -100, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 160, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 160, 150, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Bluebuff_pinkHalo.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            -1
                        }
                    }
                }
                isSingleParticle: flag = true
                emitterName: string = "Bluebuff_darkcenter"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 10, 30 }
                }
                EmitterPosition: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.600000024, 0.699999988, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 20
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -500, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -500, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 150, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_Buf_CenterGlow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 500
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Bluebuff_trailTail1"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.25
                        }
                        values: list[f32] = {
                            0.150000006
                            0
                        }
                    }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, -10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 110, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.740321994, 0, 0.736369908, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.5, 0.300000012, 0.300000012, 0.600000024 }
                            { 0.5, 0.300000012, 0.300000012, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 55, 0, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.5, 0.5 }
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_SoftEnergy_Ver.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.150000006 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "purpleWrap_sml"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -8, -30 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 180
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0.99999994, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_StormSphere_alt.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/color-bellcurve32.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.530006886, 0.429999232, 0.790005326, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.450184494
                            0.48782286
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.338002592 }
                            { 0.973876774, 0.574255764, 0.978184819, 1 }
                            { 0.959380507, 0.338002592, 0.966079175, 1 }
                            { 1, 1, 1, 0.338002592 }
                        }
                    }
                }
                pass: i16 = 6
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.958371043, 0.958371043, 0.958371043 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_dustRing_geo_tex_blue.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 2 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1.5 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/centerCutOut_maskPink.tex"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 2, 1 }
                    }
                    uvScrollAlphaMult: flag = false
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                emitterName: string = "pinkWrap_light"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 30 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_StormDome_alt.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.100007631 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.535384595
                            0.809225082
                            1
                        }
                        values: list[vec4] = {
                            { 0.125352859, 0.027359426, 0.22639811, 1 }
                            { 0.310261697, 0.137788966, 0.37956816, 1 }
                            { 0.0736400411, 0.158358127, 0.399496466, 0.835294127 }
                            { 0.13736172, 0.478110939, 1, 0.533333361 }
                            { 0.165255204, 0.514747858, 0.980880439, 0 }
                        }
                    }
                }
                pass: i16 = 5
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    1
                                }
                                keyValues: list[f32] = {
                                    360
                                }
                            }
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 0.800000012, 0.800000012 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_idle_PraxisWave_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.5 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "GlowGroundTop"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 30 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.306782633, 0.107850768, 0.500099182, 0.349019617 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -999
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 1000 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 70, 70 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_idle_Glow_01.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12.5
                }
                emitterLinger: option[f32] = {}
                emitterName: string = "electricity_purple"
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 50
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    50
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            0.821033239
                            0.935424328
                            1
                        }
                        values: list[vec4] = {
                            { 0.955046892, 0, 0.432471186, 0 }
                            { 0.979537666, 0.0407415889, 1, 1 }
                            { 0.520668328, 0.0133974217, 1, 0.882352948 }
                            { 0, 0.018997483, 0.53284502, 0.596078455 }
                            { 0.0622720681, 0.0421301611, 0.499885559, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0959409624
                                0.531365335
                                0.758302569
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                0.244343892
                                0.737556577
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_Dust_LightningSimple_erosion_4x1.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
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
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 30, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            1
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                            { 5, 5, 0 }
                            { 5, 5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_Dust_LightningSimple_4x1.tex"
                numFrames: u16 = 3
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                emitterName: string = "ribbonEnergy"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 40, 30 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.86999315, 0.400000006, 0.179995418, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.290196091, 0.180392161, 0.211764708, 0 }
                            { 0.890196085, 0.796078444, 0.549019635, 0.501960814 }
                            { 1, 0.662745118, 0.576470613, 1 }
                            { 1, 0.909803927, 0.760784328, 0.501960814 }
                            { 0.286274523, 0.192156866, 0.184313729, 0 }
                        }
                    }
                }
                pass: i16 = 20
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 60, 0.5 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_RR_dash_sub.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_SoftRibbon.tex"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                emitterName: string = "pinkWrap_Outward"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 30 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_StormDome_flipOut.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.535384595
                            0.809225082
                            1
                        }
                        values: list[vec4] = {
                            { 0.238773182, 0.00157167925, 0.0102693215, 1 }
                            { 0.348943323, 0.0814068839, 0.138750285, 1 }
                            { 0.146974906, 0.194476232, 0.750789642, 0.835294127 }
                            { 0.13736172, 1, 0.736888707, 0.533333361 }
                            { 0.239200428, 0.980880439, 0.165255204, 0 }
                        }
                    }
                }
                pass: i16 = -10
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    1
                                }
                                keyValues: list[f32] = {
                                    360
                                }
                            }
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.649999976, 0.800000012, 0.800000012 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_idle_PraxisWave_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.5 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Bluebuff_trailTail2"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.25
                        }
                        values: list[f32] = {
                            0.150000006
                            0
                        }
                    }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, -10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 110, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.269993126, 0.0200045779, 0.650003791, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.5, 0.300000012, 0.300000012, 0.600000024 }
                            { 0.5, 0.300000012, 0.300000012, 0 }
                        }
                    }
                }
                pass: i16 = -10
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 105, 0, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.5, 0.5 }
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_Purple_Trail.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12.5
                }
                emitterLinger: option[f32] = {}
                emitterName: string = "electricity_blue"
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 50
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    50
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            0.821033239
                            0.935424328
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.955046892, 0.635736644, 0 }
                            { 0.0407415889, 0.613900959, 1, 1 }
                            { 0.0533608012, 0.0133974217, 1, 0.882352948 }
                            { 0, 0.018997483, 0.53284502, 0.596078455 }
                            { 0.0622720681, 0.0421301611, 0.499885559, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0959409624
                                0.531365335
                                0.758302569
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                0.244343892
                                0.737556577
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_Dust_LightningSimple_erosion_4x1.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
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
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 40, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            1
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                            { 5, 5, 0 }
                            { 5, 5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_Dust_LightningSimple_4x1.tex"
                numFrames: u16 = 3
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1.5
                }
                emitterName: string = "GroundDrips"
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.391775399, 0.00859082956, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.391775399, 0.00859082956, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.719996929 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.550000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.719996929 }
                            { 1, 1, 1, 0.611997426 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                colorLookUpTypeY: u8 = 3
                colorLookUpScales: vec2 = { 1, 0.5 }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.25
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Splats_01_Erosion.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                depthBiasFactors: vec2 = { -1, -100 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isFollowingTerrain: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 360 }
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
                                    1
                                }
                            }
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
                            { 90, 0, 360 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 56, 0.899999976, 0.899999976 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.20000005
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 56, 0.899999976, 0.899999976 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.949999988, 0.949999988, 0.949999988 }
                            { 1, 1, 1 }
                            { 1.10000002, 1.10000002, 1.10000002 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Splats_02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "pink smoke"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 150 }
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
                            VfxProbabilityTableData {}
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
                            { 150, 250, 150 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                emissionMeshScale: f32 = 2
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 5
                }
                EmitterPosition: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.200000003 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.746898592, 0.227710381, 0.692820609, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.137850463
                            1
                        }
                        values: list[vec4] = {
                            { 0.746898592, 0.227710381, 0.692820609, 0 }
                            { 0.670190096, 0.227710381, 0.692820609, 1 }
                            { 0.746898592, 0.227710381, 0.692820609, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 35
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_SmokeErosion.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -500 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 250, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.349999994, 0.5, 0 }
                            { 1.25, 1.5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_WispySmoke01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "SRU_Blue_Skin04_idle"
        particlePath: string = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_idle"
        flags: u16 = 204
    }
    "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Spawn_JumpOut" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            50
                            100
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "Embers"
                importance: u8 = 2
                Filtering: pointer = VfxEmitterFiltering {
                    keywordsExcluded: list[string] = {
                        "AnnieFrostFire"
                        "AnnieGoth"
                    }
                }
                birthOrbitalVelocity: embed = ValueVector3 {
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
                                    -0.5
                                    1
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 2000, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 2000, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 500, 200, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 500, 200, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        250
                                        300
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        5
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.334370941, 0.136507213, 0.497993439, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.334370941, 0.136507213, 0.497993439, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.952941179, 0.952941179, 0.952941179, 0.592156887 }
                            { 0.741176486, 0.741176486, 0.741176486, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
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
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 850, 850, 850 }
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
                            1
                        }
                        values: list[vec3] = {
                            { 850, 850, 850 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 6, 2 }
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
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 6, 2 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_SandFlecks.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0
                            200
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "leaves_flewaway"
                importance: u8 = 2
                Filtering: pointer = VfxEmitterFiltering {
                    keywordsExcluded: list[string] = {
                        "AnnieFrostFire"
                        "AnnieGoth"
                    }
                }
                birthOrbitalVelocity: embed = ValueVector3 {
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
                                    -0.5
                                    1
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 200, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 300, 100, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 100, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        150
                                        325
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        5
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
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
                                            180
                                            -180
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                    0.193996757
                                    0.743804574
                                    1
                                }
                                values: list[f32] = {
                                    1
                                    0.670270264
                                    0.335135132
                                    0
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                                    0.400000006
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.209994659, 0.209994659, 0.209994659, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.386090219
                            0.828195512
                            0.992481232
                        }
                        values: list[vec4] = {
                            { 0.209994659, 0.209994659, 0.209994659, 0 }
                            { 0.209994659, 0.209994659, 0.209994659, 1 }
                            { 0.209994659, 0.209994659, 0.209994659, 1 }
                            { 0.209994659, 0.209994659, 0.209994659, 0 }
                        }
                    }
                }
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
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
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 850, 850, 850 }
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
                            1
                        }
                        values: list[vec3] = {
                            { 850, 850, 850 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 26, 6, 2 }
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
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 26, 6, 2 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Flake.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.463439912
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.931818187
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.200000003
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Shockwave"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1800, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1800, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 15, 0 }
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
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 15, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.800000012
                                            0.800999999
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0.25
                                            0.899999976
                                            0.100000001
                                            0.0500000007
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    360
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.506675839, 0.22615397, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.158861578
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.647058845, 0.675532162, 1 }
                            { 0.996078432, 0.443137258, 0.739330113, 0 }
                        }
                    }
                }
                pass: i16 = -52
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 1 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.386666656
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.386999995
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.386999995
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 200, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.226498261
                            0.480825961
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0, 0 }
                            { 0.430649698, 0.632476568, 0 }
                            { 0.334710747, 0.858938277, 0 }
                            { 0.325619847, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Nova.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Dissolve_Cloudy_01.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.200000003, 0.200000003 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 2 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1000 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1000 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "blast"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 400 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    12
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 0, 400 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 15, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 60
                    height: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0942244604, 0.270511955, 0.0177004654, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0942244604, 0.270511955, 0.0177004654, 0 }
                            { 0.0942244604, 0.270511955, 0.0177004654, 0.600000024 }
                            { 0.0848027319, 0.243462801, 0.0159305539, 0.401995897 }
                            { 0.0942244604, 0.270511955, 0.0177004654, 0 }
                        }
                    }
                }
                pass: i16 = -150
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 1.20000005
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1.20000005
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
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
                            { 50, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 1, 1 }
                            { 1, 2, 2 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Cas_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.913333297
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
                                    1.20000005
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
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "shards"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1200, 1600, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.25
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
                            { 1200, 1600, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1600, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1600, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
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
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.800000012
                                            0.800999999
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0.25
                                            0.899999976
                                            0.100000001
                                            0.0500000007
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    360
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.218125954
                            0.859248281
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 0.329411775, 0.344167233, 1 }
                            { 1, 0.179995418, 0.59313345, 1 }
                            { 1, 0, 0.812161446, 0 }
                        }
                    }
                }
                pass: i16 = -51
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 30 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_flying_shards.dds"
                numFrames: u16 = 16
                birthUvScrollRate: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, -0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 120
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.913333297
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
                                    1.20000005
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
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "upward leaves"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1200, 1600, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.25
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
                            { 1200, 1600, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1600, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1600, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
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
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.800000012
                                            0.800999999
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0.25
                                            0.899999976
                                            0.100000001
                                            0.0500000007
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    360
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.218125954
                            0.859248281
                            1
                        }
                        values: list[vec4] = {
                            { 0.800564587, 0.668604553, 0.58243686, 1 }
                            { 0.658075809, 0.55600822, 0.37830168, 1 }
                            { 0.502311766, 0.263416499, 0.194064245, 1 }
                            { 0.308049142, 0.0842908397, 0.10864424, 0 }
                        }
                    }
                }
                pass: i16 = -51
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 30 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_flying_shards.dds"
                numFrames: u16 = 16
                birthUvScrollRate: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, -0.100000001 }
                    }
                }
            }
        }
        particleName: string = "SRU_Blue_Skin04_Spawn_JumpOut"
        particlePath: string = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Spawn_JumpOut"
        flags: u16 = 198
    }
    "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_BlueBuff_Spawn_GroundSlam" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Pebbles"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 550, 0, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1200, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.800000012
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
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
                        { 0, 0, 0.99999994 }
                        { 0, 0.99999994, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.349999994, 0.349999994, 0.349999994, 1 }
                }
                isRandomStartFrame: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Particles/SRU_Krug_BA_Pebbles_4x4.dds"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.75
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
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "DustSpikes"
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    -160
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    -160
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 14, 70, 70 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 5, 5, 0 }
                            { 7, 5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Particles/SRU_BlueBuff_DustSpikes_6x1.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 6, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundBurn"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 64
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Particles/SRU_groundBurn.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                particleLinger: option[f32] = {
                    11.1999998
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundDirt"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 90 }
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
                            { 90, 1, 90 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 450, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 450, 450, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_GroundDirt.StrawberryRebuild.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1.5
                }
                isSingleParticle: flag = true
                emitterName: string = "DustCloud"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 150, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
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
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
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
                                            -90
                                            90
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
                        { 0.99999994, 0, 0 }
                        { 0, 0.99999994, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.5 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.550000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 10
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 65, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 65, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 125, 125, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 125, 125, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.649999976, 0.649999976, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Particles/SRU_dustCloud.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_dustCloud_mult.dds"
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0299999993
                rate: embed = ValueFloat {
                    constantValue: f32 = 150
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
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
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Clumps"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 700, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 600, 700, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1200, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.300000012
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
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
                        { 0, 0.99999994, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.550000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 11
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.5
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.300000012, 0.600000024 }
                            { 1, 0.5, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Particles/SRU_clumps.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    10.6000004
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "dustRing"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Particles/SRU_dustRing_geo.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.5, 0.600000024, 0.800000012, 0.300000012 }
                }
                disableBackfaceCull: bool = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 0.449999988, 1.5 }
                }
                texture: string = "ASSETS/Particles/SRU_dustRing_geo_tex.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 2 }
                }
                texDiv: vec2 = { 0.300000012, 1 }
            }
        }
        particleName: string = "SRU_BlueBuff_Spawn_GroundSlam"
        particlePath: string = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_BlueBuff_Spawn_GroundSlam"
        flags: u16 = 198
    }
    "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Spawn_GroundSlam" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Pebbles"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 550, 0, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1200, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.800000012
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
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
                        { 0, 0, 0.99999994 }
                        { 0, 0.99999994, 0 }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.580926239, 0.916746795, 1 }
                }
                isRandomStartFrame: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Krug_P_Pebbles_4x4.dds"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.75
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
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "DustSpikes"
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.705149949, 0.939406395, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    -160
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    -160
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 14, 70, 70 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 5, 5, 0 }
                            { 7, 5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_DustSpikes_6x1.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 6, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundBurn"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.681467891, 0.251407653, 0.730769813, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 0.508155942, 0.198931873, 0.721568644, 1 }
                            { 0.24213016, 0.0808880776, 0.413244843, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaRef: u8 = 64
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_groungGlow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                particleLinger: option[f32] = {
                    11.1999998
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundDirt"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.255085081, 0.101167314, 0.378652632, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 90 }
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
                            { 90, 1, 90 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 450, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 450, 450, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_GroundDirt_light.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0299999993
                rate: embed = ValueFloat {
                    constantValue: f32 = 150
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
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
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Clumps"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 700, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 600, 700, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1200, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.300000012
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
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
                        { 0, 0.99999994, 0 }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.953505754, 0.656473637, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.550000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 11
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.5
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.300000012, 0.600000024 }
                            { 1, 0.5, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_clumps.tex"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    10.6000004
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "dustRing1"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_dustRing_geo.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.409994662, 0.200000003, 0.669993162, 0.200000003 }
                }
                disableBackfaceCull: bool = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 0.449999988, 1.5 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_dustRing_geo_tex_blue.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 2 }
                }
                texDiv: vec2 = { 0.300000012, 1 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.75
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.800000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.6999998
                }
                lifetime: option[f32] = {
                    1.20000005
                }
                isSingleParticle: flag = true
                emitterName: string = "SolidBeams_cracks"
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.661509097, 0.433585107, 0.983230352, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.150000006
                                    0.400000006
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.0199999996
                                    0.200000003
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.661509097, 0.433585107, 0.983230352, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.190388173
                            0.70147872
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.991307378 }
                            { 0.989189208, 1, 1, 0.524324298 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 2.3499999, 2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    -90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2.3499999, 2, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 85, 35 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 85, 35 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 5, 3, 0 }
                            { 4, 5, 1 }
                            { 0, 7, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_Dust_LightningSimple_4x1.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/Base_GradientCard01.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                HasVariableStartTime: flag = true
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.899999976
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    0.600000024
                }
                emitterName: string = "purpleHalo"
                importance: u8 = 2
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.800000012, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 20 }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 20 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.54229039, 0.420004576, 1, 0.701960802 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0.300000012
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
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.54229039, 0.420004576, 1, 0.701960802 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.015625
                            0.416974157
                            0.681783676
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.994594574 }
                            { 0.289723039, 0.163088426, 0.440787375, 0.745098054 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -10
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 90, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1.79999995
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
                            { -90, 90, 90 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 210, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 210, 500, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.0069444445
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.767241359, 0.5, 0.767241359 }
                            { 1, 1, 1 }
                            { 0, 0.800904989, 0.76700002 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Horde_Skin04_common_light_rays_01.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_dustCloud_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 2 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "waterDrop"
                importance: u8 = 4
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -50, 35, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.00499999989
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -50, 35, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 150, 200, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1.10000002
                                    }
                                }
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
                            }
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec3] = {
                                { 150, 200, 0 }
                                { 120, 200, 0 }
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
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 20, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.890058756, 0.345769435, 0.923063993, 0.800000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -500
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 1, 1 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.381294966
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 0 }
                            { 0.294117659, 0.242028028, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                FlexInstanceScale: pointer = FlexTypeFloat {}
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Splats_02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.64999998
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                emissionSurfaceDefinition: pointer = VfxEmissionSurfaceData {
                    meshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Skin04.skn"
                    skeletonName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Skin04.skl"
                }
                emitterName: string = "shakeoff_brt"
                importance: u8 = 4
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -250, 600 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -250, 600 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 300, 160, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 20, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.890196085, 0.345098048, 0.921568632, 0.800000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -500
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -1 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                useNavmeshMask: flag = true
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 1, 1 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.381294966
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 0 }
                            { 0.294117659, 0.242028028, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                FlexInstanceScale: pointer = FlexTypeFloat {}
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Splats_02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "cast_pulse_Erode"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.423529416, 0.627451003, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.996078432, 0.996078432, 0.996078432, 0 }
                            { 0.0235294122, 0.576470613, 1, 1 }
                            { 0.741176486, 0.13333334, 1, 0 }
                        }
                    }
                }
                pass: i16 = 550
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.349999994
                                1
                            }
                            values: list[f32] = {
                                0
                                0.600000024
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 0.25
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_GroundLightning_Erosion_01.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_GroundLightning_01.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 18
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "groundfroth"
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 250
                }
                EmitterPosition: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.109803922, 0.121568628, 0.23137255, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.109803922, 0.121568628, 0.23137255, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.719996929 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.550000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.719996929 }
                            { 1, 1, 1, 0.611997426 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                colorLookUpTypeY: u8 = 3
                colorLookUpScales: vec2 = { 1, 0.5 }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.25
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Splats_01_Erosion.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                depthBiasFactors: vec2 = { -1, -100 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 360 }
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
                                    1
                                }
                            }
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
                            { 90, 0, 360 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 36, 0.899999976, 0.899999976 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
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
                            { 36, 0.899999976, 0.899999976 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.949999988, 0.949999988, 0.949999988 }
                            { 1, 1, 1 }
                            { 1.10000002, 1.10000002, 1.10000002 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Splats_02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.39999998
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Decal"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.540001512 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.101960786, 0.250980407, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.113725491, 0.101960786, 0.250980407, 0 }
                            { 0.113725491, 0.101960786, 0.250980407, 1 }
                            { 0.00909838639, 0.0081571741, 0.0200791974, 0.0899977088 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = -1
                alphaRef: u8 = 0
                censorModulateValue: vec4 = { 0.20349431, 0.0567635633, 0.305333018, 1 }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Einstein_01_mult.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 0 }
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
                            { 90, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 380, 380 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Hit01.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Nebula-erode.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.129999995
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "BurstUp_Thin"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1000, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -80, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Cylinder_01.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.444663167, 0, 1, 0.600000024 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10.1999998, 15, 10.1999998 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 1, 0.5 }
                            { 1, 1.20000005, 1 }
                            { 1, 1.5, 1 }
                            { 1.5, 1.70000005, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Water.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 3, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                        }
                        values: list[vec2] = {
                            { 3, 1 }
                            { 3, 0.200000003 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.129999995
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "MidTone"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1000, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 6, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -120, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_ConeMesh_01.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.696055532, 0.222186625, 0.407156467, 0.701960802 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.349999994
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.522331595, 0.330189973, 0.696986318, 0.541176498 }
                            { 0.297917157, 0.129350722, 0.451132983, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 40
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.600000024
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.70000005, 0.5, 1.70000005 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 1, 1 }
                            { 1.5, 2, 1.5 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Water.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -0.200000003 }
                        }
                    }
                }
                texDiv: vec2 = { 1, 2.5999999 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 3, 3 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec2] = {
                            { 3, 3 }
                            { 3, 2.4000001 }
                            { 3, 1.79999995 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.64999998
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                emissionSurfaceDefinition: pointer = VfxEmissionSurfaceData {
                    meshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Skin04.skn"
                    skeletonName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Skin04.skl"
                }
                emitterName: string = "shakeoff_drk"
                importance: u8 = 4
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -250, 620 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -250, 620 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 300, 160, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 20, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.392156869, 0.00784313772, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -500
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -1 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                useNavmeshMask: flag = true
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 1, 1 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.381294966
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 0 }
                            { 0.294117659, 0.242028028, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                FlexInstanceScale: pointer = FlexTypeFloat {}
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Splats_02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "waterDrop_drk"
                importance: u8 = 4
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -50, 35, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.00499999989
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -50, 35, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 150, 200, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1.10000002
                                    }
                                }
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
                            }
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec3] = {
                                { 150, 200, 0 }
                                { 120, 200, 0 }
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
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 20, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.392156869, 0.00784313772, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -500
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 1, 1 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.381294966
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 0 }
                            { 0.294117659, 0.242028028, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                FlexInstanceScale: pointer = FlexTypeFloat {}
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Splats_02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "SRU_Blue_Skin04_Spawn_GroundSlam"
        particlePath: string = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Spawn_GroundSlam"
        flags: u16 = 198
    }
    "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Death" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar_Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.289997697, 0.250003815, 0.540001512, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.918465257
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.989189208, 1, 1, 0.737472713 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 500
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.169265509
                                0.889688253
                            }
                            values: list[f32] = {
                                1
                                0.158371046
                                0
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/sru_blue_skin04_downTop.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.01499999, 1.01499999, 1.01499999 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/SRU_Blue_Skin04_TX_CM.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_light_wall_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec2] = {
                                { 0, 0 }
                                { 0, 0 }
                            }
                        }
                    }
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec2] = {
                                { 0, 0.5 }
                                { 0, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterName: string = "goldRiple_avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.196078435, 0, 0.298039228, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.803357303
                            1
                        }
                        values: list[vec4] = {
                            { 0.196078435, 0, 0.298039228, 1 }
                            { 0.196078435, 0, 0.298039228, 1 }
                            { 0.196078435, 0, 0.298039228, 0.905277908 }
                            { 0.196078435, 0, 0.298039228, 0 }
                        }
                    }
                }
                pass: i16 = 499
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.0500000007
                                1.04999995
                            }
                            values: list[f32] = {
                                1
                                0
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.150000006
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Death.dds"
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.01499999, 1.01499999, 1.01499999 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/color-hold.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_light_wall_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    5
                }
                lifetime: option[f32] = {
                    1.10000002
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow_ground"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 1, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.140001521, 0.0800030529, 0.179995418, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.093764998
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.140001521, 0.0800030529, 0.179995418, 0 }
                            { 0.140001521, 0.0800030529, 0.179995418, 1 }
                            { 0.140001521, 0.0800030529, 0.179995418, 1 }
                            { 0.140001521, 0.0800030529, 0.179995418, 0 }
                        }
                    }
                }
                pass: i16 = -50
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 500, 500 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 350, 350, 350 }
                            { 500, 500, 500 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_circle.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 450
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.654676259
                            1
                        }
                        values: list[f32] = {
                            450
                            289.140289
                            0
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
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
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 150, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 2000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 50
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 5
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "bits_Purple"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 100, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -150, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 200, 200, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 75, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
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
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.145098045, 0, 0.219607845, 1 }
                            { 0.669993162, 0, 1, 1 }
                            { 0.219607845, 0, 0.329411775, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            { 1, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    600
                                    -600
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    600
                                    -600
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 13, 13, 13 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                    4
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                    4
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 13, 13, 13 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.949640274
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_debris.dds"
                numFrames: u16 = 4
                startFrame: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.85000002
                rate: embed = ValueFloat {
                    constantValue: f32 = 500
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.400479615
                            1
                        }
                        values: list[f32] = {
                            500
                            441.176483
                            0
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
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
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2.5
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 150, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 2000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 50
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 5
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "bits_rot"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 100, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -150, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 200, 200, 200 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 75, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
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
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.0303807128, 0.00462348387, 0.0854047462, 1 }
                            { 0.102494851, 0.212497145, 0.346318752, 1 }
                            { 0.0903639272, 0.0709544495, 0.148516059, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            { 1, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    600
                                    -600
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    600
                                    -600
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 13, 13 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                    2.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                    2.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 13, 13 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.956834555
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_debris.dds"
                numFrames: u16 = 4
                startFrame: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar_Glow1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.970000744, 0.409994662, 0.259998471, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.918465257
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.989189208, 1, 1, 0.737472713 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 501
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.100000001
                                0.274145782
                                0.989688277
                            }
                            values: list[f32] = {
                                1
                                0.117647067
                                0
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/sru_blue_skin04_downTop.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.01499999, 1.01499999, 1.01499999 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/SRU_Blue_Skin04_TX_CM.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_light_wall_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec2] = {
                                { 0, 0 }
                                { 0, 0 }
                            }
                        }
                    }
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec2] = {
                                { 0, 0.5 }
                                { 0, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 300
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.280575544
                            1
                        }
                        values: list[f32] = {
                            300
                            111.312218
                            0
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
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
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 150, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 2000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 50
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 5
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "bits_Gold"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 100, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -3
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -150, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 200, 200, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 75, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
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
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.219607845, 0.130815595, 0, 1 }
                            { 0.819684148, 0.65819788, 0.392858773, 1 }
                            { 0.329411775, 0.182330057, 0, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            { 1, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    600
                                    -600
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    600
                                    -600
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 13, 13, 13 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                    4
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                    4
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 13, 13, 13 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.956834555
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_debris.dds"
                numFrames: u16 = 4
                startFrame: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {}
                emitterName: string = "Main_Stencil_mask"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 55, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 55, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 5, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeCylinder {}
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    UseAvatarSpecificSubmeshMask: bool = true
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 0.200000003 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.373021603
                            0.800000012
                            0.9472422
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.994594574, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 99
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.131894484
                                0.262826204
                                0.580335736
                                1
                            }
                            values: list[f32] = {
                                0.600834608
                                0.600834608
                                0.671701252
                                0.907600582
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/Skin04_VGU_Generic_Erosion01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                stencilMode: u8 = 1
                stencilRef: u8 = 4
                particleIsLocalOrientation: flag = true
                useNavmeshMask: flag = true
                SortEmittersByPos: flag = true
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.949999988, 0.953999996, 0.949999988 }
                            { 1.5, 1.20000005, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/common_color-hold.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                texDiv: vec2 = { 0.449999988, 0.449999988 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 80
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "GLOW_dk"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 65, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 500, 350, 1 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.731414855
                            1
                        }
                        values: list[vec4] = {
                            { 0.481925696, 0.0898298621, 0.549050152, 0 }
                            { 0.216037229, 0.0805828944, 0.340077817, 1 }
                            { 0.237216756, 0.00674448768, 0.0566414893, 0.701960802 }
                            { 0.137788966, 0, 0.0680704936, 0 }
                        }
                    }
                }
                pass: i16 = 600
                colorLookUpTypeY: u8 = 3
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.400479615
                                1
                            }
                            values: list[f32] = {
                                0
                                0.375565618
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/3026_Items_Streaks.dds"
                }
                stencilMode: u8 = 2
                stencilRef: u8 = 4
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 60, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00239808159
                            0.65933609
                            1
                        }
                        values: list[vec3] = {
                            { 0.988687754, 1, 1 }
                            { 1.24034536, 1.23303163, 1.23755658 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/NE_Core_Mask.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/Skin04_Energy_Mult01.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[f32] = {
                            2
                            2
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Smoke_BurstInner"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 120 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 120 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0, -150 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, -150 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                { 0, 0, 0 }
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
                                            -80
                                            80
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
                        { 0, 1, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.219607845, 0.203921571, 0.352941185, 0.741176486 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.219607845, 0.203921571, 0.352941185, 0.741176486 }
                            { 0.219607845, 0.203921571, 0.352941185, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                0.699999988
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_SmokeErosion.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -100 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 100, 100 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 100, 100 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.100000001, 0.100000001 }
                            { 0.699999988, 0.699999988, 0.699999988 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_WispySmoke01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Mesh_SMoke"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Sphere_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.914168, 0.315373451, 0.797695875, 0 }
                            { 0.603921592, 0.399725348, 0.899793983, 1 }
                            { 0.100007631, 0.059998475, 0.400000006, 0.500007629 }
                            { 0.100007631, 0.059998475, 0.330006868, 0.0699931309 }
                            { 0.0907759219, 0.0566262305, 0.360646993, 0 }
                        }
                    }
                }
                pass: i16 = 150
                alphaRef: u8 = 1
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Particles_1_1578.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 5
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 5, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 4, 5, 5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.300000012, 0.600000024 }
                            { 1.10000002, 2, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Wisp_Trail3.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { -1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec2] = {
                            { -1, 0 }
                            { -0.300000012, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 3 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -50
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Ey9.dds"
                    texAddressModeMult: u8 = 2
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1.5 }
                    }
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 2 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.800000012
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                                0.5
                            }
                            values: list[vec2] = {
                                { 0, 2 }
                                { 0, 0.200000003 }
                            }
                        }
                    }
                    birthUvRotateRateMult: embed = ValueFloat {
                        constantValue: f32 = -50
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.200000003 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    2.5
                }
                emitterName: string = "BurstSmokeOut"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 900, 500, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
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
                                    0
                                }
                            }
                        }
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
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.961776137, 0.511116207, 0.932188928, 0.741176486 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.961776137, 0.511116207, 0.932188928, 0.741176486 }
                            { 0.961776137, 0.511116207, 0.932188928, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                0.699999988
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_SmokeErosion.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 75, 50, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_WispySmoke01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    3
                }
                emitterName: string = "SmokePoofMain"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 150 }
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
                            VfxProbabilityTableData {}
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
                            { 150, 250, 150 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 50, 50 }
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
                                VfxProbabilityTableData {}
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
                                { 50, 50, 50 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.250003815, 0.110002287, 0.560006082, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.250003815, 0.110002287, 0.560006082, 0.800000012 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 35
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_SmokeErosion.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -500 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 250, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.349999994, 0.5, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_WispySmoke01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 47
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.949999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.800000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.75
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Feathers"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -2500, 0 }
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
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
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
                            { 0, -2500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 100
                    height: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.137254909, 0.117647059, 0.203921571, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.972549021, 0.847059011, 0.800000012 }
                            { 1, 0.945097983, 0.772548974, 1 }
                            { 1, 0.992156982, 0.952941, 1 }
                            { 1, 0.992156982, 0.968626976, 1 }
                        }
                    }
                }
                pass: i16 = -20
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 24, 24, 7 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.25
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 24, 24, 7 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 3, 1 }
                            { 1, 3, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Ash.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.70000005
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundCoruption"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.730006874 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.160006106, 0.149996191, 0.269993126, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.160006106, 0.149996191, 0.269993126, 1 }
                            { 0.160006106, 0.149996191, 0.269993126, 1 }
                            { 0.0704017133, 0.0539995432, 0.167396978, 0 }
                        }
                    }
                }
                pass: i16 = -5600
                meshRenderFlags: u8 = 0
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.5
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.0599999987
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Particles_1_1578.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isFollowingTerrain: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 1, 0 }
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
                            { -90, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 180, 540 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 450, 180, 540 }
                            { 0, 180, 540 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1.79999995
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                period: option[f32] = {
                    0.100000001
                }
                timeActiveDuringPeriod: option[f32] = {
                    0.200000003
                }
                emitterName: string = "DeathParticlesEdge"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.300000012, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 450, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 450, 0 }
                        }
                    }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 600 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                { 0, 0, 600 }
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
                                            -80
                                            80
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
                        { 0, 1, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.449999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.615686297, 0.953749895, 1 }
                            { 0.429999232, 0.310002297, 1, 0.549996197 }
                            { 0.0143739991, 0.0411383249, 0.629633009, 0.411764711 }
                            { 0.217151135, 0, 0.667811096, 0.380392164 }
                        }
                    }
                }
                pass: i16 = 5
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30.9375, 0.5625, 0.5625 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 30.9375, 0.5625, 0.5625 }
                            { 24.75, 0.450000018, 0.450000018 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Ash.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 13
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.70000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.70000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "FIRE"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 250, 50 }
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
                            VfxProbabilityTableData {}
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
                            { 25, 250, 50 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 500 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 200
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.760784328, 0.403921574, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.760784328, 0.403921574, 1, 1 }
                            { 0.760784328, 0.403921574, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 35
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.0500000007
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_SmokeErosion.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0.500007629, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -500 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 250, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.349999994, 0.5, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_WispySmoke01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Base_SmokeErode.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.913333297
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
                                    1.20000005
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
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "shards"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1200, 1600, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.25
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
                            { 1200, 1600, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1600, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1600, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
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
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.800000012
                                            0.800999999
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0.25
                                            0.899999976
                                            0.100000001
                                            0.0500000007
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    360
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.218125954
                            0.859248281
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 0.329411775, 0.344167233, 1 }
                            { 1, 0.179995418, 0.59313345, 1 }
                            { 1, 0, 0.812161446, 0 }
                        }
                    }
                }
                pass: i16 = -51
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 30 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_flying_shards.dds"
                numFrames: u16 = 16
                birthUvScrollRate: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, -0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 120
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.913333297
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
                                    1.20000005
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
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "upward leaves"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1200, 1600, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.25
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
                            { 1200, 1600, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1600, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1600, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
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
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.800000012
                                            0.800999999
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0.25
                                            0.899999976
                                            0.100000001
                                            0.0500000007
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    360
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.218125954
                            0.859248281
                            1
                        }
                        values: list[vec4] = {
                            { 0.800564587, 0.668604553, 0.58243686, 1 }
                            { 0.658075809, 0.55600822, 0.37830168, 1 }
                            { 0.502311766, 0.263416499, 0.194064245, 1 }
                            { 0.308049142, 0.0842908397, 0.10864424, 0 }
                        }
                    }
                }
                pass: i16 = -51
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 30 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_flying_shards.dds"
                numFrames: u16 = 16
                birthUvScrollRate: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, -0.100000001 }
                    }
                }
            }
        }
        particleName: string = "SRU_Blue_Skin04_Death"
        particlePath: string = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Death"
        flags: u16 = 198
    }
    "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_BA_1_FistSlam" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Pebbles"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 550, 0, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1200, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.800000012
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
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
                        { 0, 0, 0.99999994 }
                        { 0, 0.99999994, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.349999994, 0.349999994, 0.349999994, 1 }
                }
                isRandomStartFrame: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Krug_BA_Pebbles_4x4.dds"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.75
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
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "DustSpikes"
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    -160
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    -160
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 14, 70, 70 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 5, 5, 0 }
                            { 7, 5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_DustSpikes_6x1.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 6, 1 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.75
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.699999988
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.6999998
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "SolidBeams"
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.100000001, 0.600000024, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.100000001, 0.600000024, 1, 0 }
                            { 0.100000001, 0.600000024, 1, 1 }
                            { 0.100000001, 0.600000024, 1, 0 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -70
                                    -110
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -70
                                    -110
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 70, 70 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 70, 70 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 5, 3, 0 }
                            { 4, 5, 1 }
                            { 0, 7, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_Dust_Jets_4x1.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.899999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.75
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.899999976
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.8999996
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "SoftBeams"
                primitive: pointer = VfxPrimitiveRay {}
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.617502093, 0.100007631, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.617502093, 0.100007631, 1, 0 }
                            { 0.617502093, 0.100007631, 1, 1 }
                            { 0.617502093, 0.100007631, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -70
                                    -110
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -70
                                    -110
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 70, 70 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 70, 70 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 5, 3, 0 }
                            { 3, 5, 1 }
                            { 0, 7, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_BlueBuff_SoftRays_1x4.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.25
                }
                particleLinger: option[f32] = {
                    11.25
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundBurn"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.200000003
                            0.739852369
                            1
                        }
                        values: list[vec4] = {
                            { 0.393560708, 0.14837873, 0.14837873, 0 }
                            { 1, 0.330403596, 0.48943314, 1 }
                            { 0.357167929, 0.146715492, 0.352437615, 1 }
                            { 0.142366678, 0.0213015955, 0.230441749, 0.686274529 }
                            { 0.0749828368, 0, 0.178820476, 0 }
                        }
                    }
                }
                pass: i16 = 200
                alphaRef: u8 = 64
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 175, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_groungGlow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    11.5
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundDirt"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 5, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.438223839, 0.581109345, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 90 }
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
                            { 90, 1, 90 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 255, 255, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 255, 255, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_GroundDirt.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1.5
                }
                isSingleParticle: flag = true
                emitterName: string = "DustCloud"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -100, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
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
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
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
                                            -90
                                            90
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
                        { 0.99999994, 0, 0 }
                        { 0, 0.99999994, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.550000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 10
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 65, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 65, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 125, 125, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 125, 125, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.649999976, 0.649999976, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_dustCloud.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_dustCloud_mult.dds"
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0299999993
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
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
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Clumps"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 1450, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 1450, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -2000, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -2000, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.300000012
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
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
                        { 0, 0.99999994, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.550000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 11
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.5
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.300000012, 0.600000024 }
                            { 1, 0.5, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_clumps.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    10.6000004
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "dustRing"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_dustRing_geo.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.770000756, 0.489997715, 0.940001547, 0.300007641 }
                }
                disableBackfaceCull: bool = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0.300000012, 1 }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_dustRing_geo_tex.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 2 }
                }
                texDiv: vec2 = { 0.300000012, 1 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundCracks"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 10, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
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
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 60.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 60.5, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            1
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                            { 5, 5, 0 }
                            { 5, 5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_groundCracks_3x1.dds"
                numFrames: u16 = 3
                texDiv: vec2 = { 3, 1 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_dustCloud_mult.dds"
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.75
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.75
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11.75
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "RockShards"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 60, -5, 0 }
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
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 60, -5, 0 }
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
                                            90
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
                        { 0.99999994, 0, 0 }
                        { 0, 0.99999994, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/Generic_RockShards_01.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/Generic_RockShards_01.skl"
                        mAnimationName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/Generic_Rockshards_01.anm"
                    }
                }
                blendMode: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 0.823224247, 0.957518876, 1 }
                            { 0.946150899, 0.760830104, 1, 0.600000024 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 18
                disableBackfaceCull: bool = true
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 35, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500100017
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    -1
                                    -1
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
                                    0.5
                                    0.500100017
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    -1
                                    -1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_RockShards.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Sparkles"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.289575279
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 80, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 80, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                    }
                                    keyValues: list[f32] = {
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
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
                        { 0, 0, 1.00000012 }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.540001512, 0.409994662, 0.730006874, 0.590005338 }
                }
                pass: i16 = -5
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -300, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 65, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.75
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
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
                            { 30, 65, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/Flecks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.699999988
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "ShadowWisps"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                EmitterPosition: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.105882354, 0.0784313753, 0.152941182, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.349999994
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.0980392173 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Smoke_01.dds"
                }
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 120, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 120, 30 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.75, 0.200000003, 0.200000003 }
                            { 1.5, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/3026_Items_Noise_02.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.300000012, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.300000012, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 2 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/3026_Items_glow_03.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "MatterDissolve_SW"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 900, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.289575279
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 900, 50, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 80, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 80, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 100
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.492286563, 0.294117659, 0.525490224, 0.592156887 }
                }
                pass: i16 = -5
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -300, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 65, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.75
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
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
                            { 30, 65, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/Flecks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            10
                            5
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.25
                            0.125
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.649999976
                }
                emitterName: string = "distort_blast"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_alpha_20.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -9999
                meshRenderFlags: u8 = 0
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.00100000005
                    distortionMode: u8 = 3
                    normalMapTexture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_distort-ripples.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 550, 550 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 200, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.349999994, 0.349999994, 0.349999994 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterName: string = "Tenticles_omni"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Tendril.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.4541848, 0.4541848, 0.4541848, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.4541848, 0.4541848, 0.4541848, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.951506853, 0.330296785, 0.969619274, 0 }
                            { 0.559822977, 0.259174496, 0.851956964, 1 }
                            { 0.136430919, 0.0935072899, 0.340184629, 0 }
                        }
                    }
                }
                pass: i16 = -50
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Beam_Edge_Mult.dds"
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    30
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 20, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                            { 2.20000005, 2.5999999, 2.20000005 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.349999994
                            1
                        }
                        values: list[vec3] = {
                            { 3.75, 0.899999976, 0.75 }
                            { 5.5, 1.10000002, 1.10000002 }
                            { 4.5, 1.20000005, 0.899999976 }
                            { 2.5, 1.5, 0.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/SRU_Blue_Skin04_Smokey_beam.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.5 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/SRU_Blue/Skins/Skin04/Particles/Base_GradientCard01.dds"
                }
            }
        }
        particleName: string = "SRU_Blue_Skin04_BA_1_FistSlam"
        particlePath: string = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_BA_1_FistSlam"
    }
    0x632e5ade = GearSkinUpgrade {
        mGearData: pointer = GearData {
            mVFXResourceResolver: pointer = ResourceResolver {
                resourceMap: map[hash,link] = {
                    0xa7fa0054 = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_BlueBuff_Spawn_GroundSlam"
                }
            }
            mCharacterSubmeshesToHide: list[hash] = {
                "Corrupted"
            }
            mCharacterSubmeshesToShow: list[hash] = {
                "normal"
            }
            EnableOverrideIdleEffects: bool = true
            OverrideIdleEffects: list[embed] = {
                SkinCharacterDataProperties_CharacterIdleEffect {
                    effectName: string = "SRU_BlueBuff_idle.troy"
                    boneName: string = "Buffbone_Cstm_BlueBuff"
                }
            }
        }
    }
    0xc7020d4f = GearSkinUpgrade {
        mGearData: pointer = GearData {
            mVFXResourceResolver: pointer = ResourceResolver {}
            mCharacterSubmeshesToHide: list[hash] = {
                "normal"
            }
            mCharacterSubmeshesToShow: list[hash] = {
                "Corrupted"
            }
            EnableOverrideIdleEffects: bool = true
            OverrideIdleEffects: list[embed] = {
                SkinCharacterDataProperties_CharacterIdleEffect {
                    effectKey: hash = "neutralmonster_buf_blue_defense_big.troy"
                    boneName: string = "Root"
                }
            }
        }
    }
    "Characters/SRU_Blue/Skins/Skin4/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0x111df920 = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_BA_3_FistSlam"
            0x98178d7c = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Idle_DragonState"
            "SRU_Blue_BA_Void_Transform" = "Characters/SRU_Blue/Skins/Skin0/Particles/SRU_Blue_Base_BA_Void_Transform"
            "SRU_Blue_Buff_Get" = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Buff_Get"
            0x2aed8ee6 = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_BA_1_FistSlam"
            "SRU_Blue_Skin04_idle" = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_idle"
            0x077503d1 = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Death"
            0xa7fa0054 = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Spawn_GroundSlam"
            0x2fdee4d4 = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_Blue_Skin04_Spawn_JumpOut"
            "SRU_BlueBuff_Spawn_GroundSlam" = "Characters/SRU_Blue/Skins/Skin4/Particles/SRU_BlueBuff_Spawn_GroundSlam"
        }
    }
}
