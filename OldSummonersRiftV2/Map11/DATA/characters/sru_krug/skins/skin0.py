#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/SRU_Krug/SRU_Krug.bin"
    "DATA/Characters/SRU_Krug/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/SRU_Krug/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "SRU_Krug"
        emoteLoadout: hash = 0xd3eee753
        skinAudioProperties: embed = skinAudioProperties {
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "NPC_Map11_Krug_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Krug_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Krug_SFX_events.bnk"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/SRU_Krug/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/SRU_Krug/Skins/Base/SRU_Krug.skl"
            simpleSkin: string = "ASSETS/Characters/SRU_Krug/Skins/Base/SRU_Krug.skn"
            texture: string = "ASSETS/Characters/SRU_Krug/Skins/Base/SRU_Krug_Base_TX_CM.dds"
            skinScale: f32 = 1.54999995
            selfIllumination: f32 = 0.699999988
            material: link = "Characters/SRU_Krug/Skins/Skin0/Materials/SR_GoldenKrug"
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Stone"
        iconCircle: option[string] = {
            "AncientKrug_Circle.dds"
        }
        iconSquare: option[string] = {
            "AncientKrug_Square.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 5
        }
        mResourceResolver: link = "Characters/SRU_Krug/Skins/Skin0/Resources"
    }
    "Characters/SRU_Krug/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "SRU_Krug_Spawn_Impact" = "Characters/SRU_Krug/Skins/Skin0/Particles/SRU_Krug_Spawn_Impact"
            "SRU_Krug_Spawn_Mis" = "Characters/SRU_Krug/Skins/Skin0/Particles/SRU_Krug_Spawn_Mis"
        }
    }
    "Characters/SRU_Krug/Skins/Skin0/Particles/SRU_Krug_Spawn_Mis" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "krugMesh"
                keywordsExcluded: list[string] = {
                    "SRU_Krug_BloodMoon"
                    "SRU_KrugMini_BloodMoon"
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/SRU_KrugMini/Skins/Base/Particles/SRU_Krugs_Mis_Mesh.scb"
                    }
                }
                blendMode: u8 = 3
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.0500000007
                    fresnelColor: vec4 = { 0.337254912, 0.192156866, 0.0352941193, 0 }
                }
                isUniformScale: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 100, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            { 300, 100, 100 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.25, 1, 1 }
                }
                texture: string = "ASSETS/Characters/SRU_Krug/Skins/Base/SRU_KrugMini_base_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "glow"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.298038989 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.298038989 }
                            { 1, 0.819607854, 0.270588249, 0.298038989 }
                            { 1, 0.576470613, 0.152941182, 0 }
                        }
                    }
                }
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -200
                                    200
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
                    constantValue: vec3 = { 100, 100, 250 }
                }
                texture: string = "ASSETS/Characters/SRU_KrugMini/Skins/Base/Particles/Item_HextechRevolver_Cyan_Glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "Trail"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 4000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 400, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.400000006 }
                            { 0, 0.400000006, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.600000024, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_KrugMini/Skins/Base/Particles/SG_Lulu_Skin07_Homeguard_trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.200000003, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 0.330000013, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
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
                            0.600000024
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.6000004
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "smoke"
                shape: embed = VfxShape {
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
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.74901998, 0.74901998, 0.74901998, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.74901998, 0.74901998, 0.74901998, 0 }
                            { 0.74901998, 0.74901998, 0.74901998, 0.800000012 }
                            { 0.74901998, 0.74901998, 0.74901998, 0 }
                        }
                    }
                }
                pass: i16 = -5
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_KrugMini/Skins/Base/Particles/SRU_Krug_Spawn_Smoke.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
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
                    0.200000003
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "sparks"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 20, 20 }
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
                                { 20, 20, 20 }
                            }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.772549033, 0.376470596, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.772549033, 0.376470596, 0.400000006 }
                            { 1, 0.772549033, 0.376470596, 0.400000006 }
                            { 1, 0.772549033, 0.376470596, 0.400000006 }
                            { 1, 0.772549033, 0.376470596, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 120, 1.20000005 }
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
                            { 25, 120, 1.20000005 }
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
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_KrugMini/Skins/Base/Particles/SRU_Sigil_Motes_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "SRU_Krug_Spawn_Mis"
        particlePath: string = "Characters/SRU_Krug/Skins/Skin0/Particles/SRU_Krug_Spawn_Mis"
        soundOnCreateDefault: string = "Play_sfx_SRU_Krug_golden_impact_cast"
    }
    "Characters/SRU_Krug/Skins/Skin0/Particles/SRU_Krug_Spawn_Impact" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
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
                                    0.75
                                    1.5
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
                    1
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "smokeRing"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 0, 300 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 0, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 10, 0, 10 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 15, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.737254977, 0.737254977, 0.737254977, 0.400000006 }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.349999994
                                1
                            }
                            values: list[f32] = {
                                1.10000002
                                0.300000012
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.800000012
                    erosionSliceWidth: f32 = 1.60000002
                    erosionMapName: string = "ASSETS/Characters/SRU_Krug/Skins/Base/Particles/GlobalCamouflage_erosion_mult.dds"
                    erosionMapAddressMode: u8 = 0
                }
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -60
                                    60
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
                    constantValue: vec3 = { 40, 40, 40 }
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
                            { 40, 40, 40 }
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
                            { 0.5, 0.5, 1 }
                            { 1.5, 1.5, 1.5 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Krug/Skins/Base/Particles/SRU_Krug_Spawn_Smoke.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 80
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
                                    0.300000012
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
                    0.200000003
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                emitterName: string = "sparks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 600, 600 }
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
                                    -0.200000003
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
                            { 600, 600, 600 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 10, 10, 10 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 100, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.811764717, 0.505882382, 0.450980395 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.582560539, 0, 0.450980395 }
                            { 1, 0.735363305, 0.285674751, 0.450980395 }
                            { 1, 0.553910017, 0.162675887, 0.450980395 }
                            { 0.56078434, 0.251487881, 0.0456286035, 0 }
                        }
                    }
                }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 120, 1.20000005 }
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
                            { 40, 120, 1.20000005 }
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
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Krug/Skins/Base/Particles/SRU_Sigil_Motes_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Flash_Mult1"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 100, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.427451015 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.925490201, 0.768627465, 0.427451015 }
                            { 1, 0.709803939, 0.376470596, 0.427451015 }
                            { 0.847058833, 0.376470596, 0.0666666701, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 1.5, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Krug/Skins/Base/Particles/Item_HextechRevolver_Cyan_Glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 80
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
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
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                emitterName: string = "debris"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 800, 500 }
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 500, 800, 500 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -5000, 0 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -5000, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 100, 100 }
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
                                        0.5
                                        1
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
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
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 100, 1 }
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
                            { 40, 100, 1 }
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
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Krug/Skins/Base/Particles/Siege_SiegeCannon_ImpactIllaoi_Base_BA_dirt_rock.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "SRU_Krug_Spawn_Impact"
        particlePath: string = "Characters/SRU_Krug/Skins/Skin0/Particles/SRU_Krug_Spawn_Impact"
    }
    "Characters/SRU_Krug/Skins/Skin0/Materials/SR_GoldenKrug" = StaticMaterialDef {
        name: string = "Characters/SRU_Krug/Skins/Skin0/Materials/SR_GoldenKrug"
        defaultTechnique: string = "normal"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Characters/SRU_Krug/Skins/Base/SRU_Krug_Base_TX_CM.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Characters/SRU_Krug/Skins/Base/SRU_Krug_Base_TX_Mask.dds"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "EmmisiveFactor"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Intensity"
                value: vec4 = { 0.150000006, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Color"
                value: vec4 = { 1, 0.552941203, 0.00784313772, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Value"
                value: vec4 = { 1.28799999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Texture_Scroll_Speed"
                value: vec4 = { 0.100000001, 0.300000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Tile"
                value: vec4 = { 3, 6, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Texture_Glow_Min_Max"
                value: vec4 = { 1, 4, 0, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "ENABLE_MASK_FX"
            }
        }
        shaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/SkinnedMesh/SR_GoldenKrug"
                    }
                }
            }
        }
        childTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                name: string = "transition"
                parentName: string = "normal"
                shaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "Glow_Intensity"
                    driver: pointer = SineMaterialDriver {
                        mDriver: pointer = TimeMaterialDriver {}
                        mFrequency: f32 = 2
                        mScale: f32 = 0.25
                        mBias: f32 = 0.5
                    }
                }
                DynamicMaterialParameterDef {
                    name: string = "EmmisiveFactor"
                    driver: pointer = BlendingSwitchMaterialDriver {
                        mElements: list[embed] = {
                            SwitchMaterialDriverElement {
                                mCondition: pointer = IsDeadDynamicMaterialBoolDriver {}
                                mValue: pointer = FloatLiteralMaterialDriver {}
                            }
                        }
                        mDefaultValue: pointer = FloatLiteralMaterialDriver {
                            mValue: f32 = 0.600000024
                        }
                    }
                }
            }
        }
    }
}
