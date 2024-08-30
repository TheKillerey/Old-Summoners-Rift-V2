#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/sru_dragon_hextech/sru_dragon_hextech.bin"
    "DATA/Characters/sru_dragon_hextech/Animations/Skin0.bin"
}
entries: map[hash,embed] = {
    "Characters/sru_dragon_hextech/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "sru_dragon_hextech"
        metaDataTags: string = "monstertype:dragon"
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "SRU_Dragon_Hextech"
            }
            bankUnits: list2[embed] = {
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
                BankUnit {
                    name: string = "NPC_Map11_Dragons_Hextech_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_Hextech_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Shared/NPC_Map11_Dragons_Hextech_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_SRU_Dragon_Hextech_HextechAttack_buffactivate"
                        "Play_sfx_SRU_Dragon_Hextech_HextechAttack_cast"
                        "Play_sfx_SRU_Dragon_Hextech_HextechAttack_hit"
                        "Play_vo_SRU_Dragon_Hextech_Attack_OnCast"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/sru_dragon_hextech/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/sru_dragon_hextech.skl"
            simpleSkin: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/sru_dragon_hextech.skn"
            texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/SRU_Dragon_Hextech_TX_CM.dds"
            skinScale: f32 = 3
            selfIllumination: f32 = 0.699999988
            brushAlphaOverride: f32 = 1
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Flesh"
        iconCircle: option[string] = {
            "ASSETS/Characters/sru_dragon_hextech/HUD/Icons2D/Dragon_Circle_Hextech.dds"
        }
        iconCircleScale: option[f32] = {
            1.20000005
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/sru_dragon_hextech/HUD/Icons2D/Dragon_Square_Hextech.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            hpPerTick: f32 = 1000
            attachToBone: string = "Buffbone_Cstm_Healthbar"
            unitHealthBarStyle: u8 = 5
        }
        mResourceResolver: link = "Characters/sru_dragon_hextech/Skins/Skin0/Resources"
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_Base_BA_Empowered_Beam" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.119999997
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.239999995
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Lightning1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 600, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.39000535, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.39000535, 1, 1 }
                            { 0, 0.372657895, 1, 1 }
                            { 0, 0.310653389, 1, 1 }
                            { 0, 0.249601036, 1, 1 }
                        }
                    }
                }
                pass: i16 = 100
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
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00510204071
                            0.143153891
                            0.418306589
                            1
                        }
                        values: list[vec3] = {
                            { 0.494565219, 1, 0 }
                            { 1.1812973, 1, 1 }
                            { 1.83639526, 1, 1 }
                            { 1.9658258, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 3
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { -2, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec2] = {
                            { -2, 0 }
                            { -0.400000006, 0 }
                            { -0, 0 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_GroundBurst.dds"
                    texDivMult: vec2 = { 4, 1 }
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                    }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -3 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, -3 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
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
                                        1
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
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.119999997
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Charged_Beam_Lightning2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 400, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0948195606, 0.461722732, 1, 1 }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.600000024
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 18, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00510204071
                            0.134693876
                            0.40646258
                            1
                        }
                        values: list[vec3] = {
                            { 0.494565219, 1, 0 }
                            { 1.30978262, 1, 1 }
                            { 2.15760875, 1, 1 }
                            { 2.3641305, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 4
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.200000003, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { -0.200000003, 0 }
                            { -0, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 1 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_GroundBurst.dds"
                    texDivMult: vec2 = { 4, 1 }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -1.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, -1.5 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
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
                                        1
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
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Lightning3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 800, 0 }
                        }
                        mAnimatedColorWithDistance: embed = ValueColor {
                            constantValue: vec4 = { 1, 0, 0, 1 }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.0934462473, 0.352208734, 1 }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 6
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_GroundBurst.dds"
                    texDivMult: vec2 = { 4, 1 }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 3 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 3 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
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
                                        1
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
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Base"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 500, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.420004576 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.41115436, 0, 0.547722578, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.41115436, 0, 0.317676574, 0 }
                            { 0.0524929948, 0, 0.547722578, 1 }
                            { 0, 0, 0.203326389, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.119623654
                            0.911290348
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.07865167, 0, 0 }
                            { 1.5, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_Mult01.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.889999986, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.889999986, 0 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Base1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.400671393, 0, 1, 1 }
                            { 0.0233005267, 0.164461732, 0.624414444, 0.772549033 }
                            { 0, 0.0259861145, 0.371221483, 0 }
                        }
                    }
                }
                pass: i16 = 25
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 1, 1 }
                }
                texture: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0799999982
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.119999997
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Base2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.114091709, 0.506111264, 1, 1 }
                }
                pass: i16 = 125
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ProjectileBeam.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -4.5, 0 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0799999982
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.0500000007
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "NegativeLightning"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 800, 0 }
                        }
                        mAnimatedColorWithDistance: embed = ValueColor {
                            constantValue: vec4 = { 1, 0, 0, 1 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.0934462473, 0.352208734, 1 }
                }
                pass: i16 = 120
                alphaRef: u8 = 250
                sliceTechniqueRange: f32 = 80
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 6
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
                texDiv: vec2 = { 4, 1 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Base3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.10391394, 0.378713667, 1, 1 }
                }
                pass: i16 = 25
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.0583333336
                            0.257954419
                            0.558211505
                            1
                        }
                        values: list[vec3] = {
                            { 4, 0, 0 }
                            { 3.24705887, 0, 0 }
                            { 1.54705882, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.0799999982
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Lightning5"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 800, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.324956119, 0.80895704, 1, 1 }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.726950288
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 4
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -1, 0 }
                }
                texDiv: vec2 = { 4, 1 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0799999982
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.0299999993
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Base4"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0169832911, 0, 0.0999160782, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.00781228812, 0, 0.0999160782, 0.289997697 }
                            { 0.00543460157, 0, 0.0999160782, 1 }
                            { 0, 0, 0.0999160782, 0.960006118 }
                        }
                    }
                }
                pass: i16 = 120
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 4, 0, 0 }
                            { 3, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
        }
        particleName: string = "SRU_Dragon_Hextech_Base_BA_Empowered_Beam"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_Base_BA_Empowered_Beam"
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_BA_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    3
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Ground_Glow"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.209994659 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0649717525
                            0.265536726
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.582391083, 0.349019617, 1, 1 }
                            { 0.0500038154, 0.560006082, 1, 1 }
                            { 0, 0.383993298, 1, 1 }
                            { 0, 0.400503546, 1, 0 }
                        }
                    }
                }
                pass: i16 = 47
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 220, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "Floor_DarkGlow"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0500038154, 0.0699931309, 0.149996191, 0.300007641 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -50
                meshRenderFlags: u8 = 0
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    11
                }
                isSingleParticle: flag = true
                emitterName: string = "Hit_Small_dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                    constantValue: vec4 = { 0.0614785999, 0.120286867, 0.264957666, 0.800000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.12785235
                            0.324205816
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 2, 0, 0 }
                            { 1.09276009, 0, 0 }
                            { 0.65882355, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.949999988
                }
                particleLinger: option[f32] = {
                    11
                }
                isSingleParticle: flag = true
                emitterName: string = "Hit_Small_dark1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.549996197 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.373830765, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.158000007
                            0.248000011
                            0.418333322
                            0.54733336
                            0.716000021
                            0.878666639
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 1, 1 }
                            { 0, 0.225855738, 1, 1 }
                            { 0, 0.225829527, 1, 0.298507452 }
                            { 0, 0.225779906, 1, 0.111940302 }
                            { 0, 0.225792989, 1, 0.156862751 }
                            { 0, 0.136201382, 1, 0.188235298 }
                            { 0, 0.132961333, 1, 0.0901960805 }
                            { 0, 0.0635515153, 1, 0 }
                        }
                    }
                }
                pass: i16 = 150
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.209205806
                            0.394205809
                            1
                        }
                        values: list[vec3] = {
                            { 1.54999995, 0, 0 }
                            { 1.14511311, 0, 0 }
                            { 0.582352936, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Items/8001/Particles/bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.100000001
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.25
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                emitterName: string = "RandomArcs"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -50, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
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
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_BA_LightningMesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.308339059, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.300000012
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 0 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 0 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 1 }
                        }
                    }
                }
                pass: i16 = 99
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
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 360, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 0.400000006, 0.349999994 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.75, 0.400000006, 0.349999994 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.26836735
                            0.381292522
                            0.521428585
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 0.971467376, 1 }
                            { 1, 0.498641312, 1 }
                            { 1, 0.756793499, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                numFrames: u16 = 4
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
                                    -1
                                    1
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
                texDiv: vec2 = { 4, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                    constantValue: vec4 = { 0, 0.394995034, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.200000003
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.346976042, 0.513725519, 1 }
                            { 0, 0.131646931, 0.97294575, 1 }
                            { 0, 0.29624477, 1, 0.200000003 }
                        }
                    }
                }
                pass: i16 = 151
                miscRenderFlags: u8 = 1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 1.5, 1.5, 1.5 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_Shockwave01_Color.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 50
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        50
                                    }
                                }
                            }
                            axisFraction: vec3 = { 2.10599995, 0.702000022, 2.10599995 }
                        }
                    }
                }
                emitterName: string = "Glow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 800, 150, 0 }
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
                            { 800, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 6, 6 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 25, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.19047837, 0.408651859, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.19047837, 0.408651859, 1, 1 }
                            { 0.19047837, 0.408651859, 1, 0.170000762 }
                            { 0.19047837, 0.408651859, 1, 0.0899977088 }
                            { 0.19047837, 0.408651859, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.29280898
                            0.39112246
                            0.530656874
                            0.640593112
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 0.423913032, 0 }
                            { 0.311764717, 0.731967747, 0 }
                            { 0.65882355, 0.629096627, 0 }
                            { 0.452941179, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.144999996
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
                            0.144999996
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {}
                emitterName: string = "DirectionalSparks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 900, 0, 0 }
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
                            { 900, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.354543388, 0.703196764, 1, 1 }
                            { 0, 0.434500635, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 22, 100, 96 }
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
                            { 22, 100, 96 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.350337088
                            0.496629
                            0.712359428
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.0117647061, 0 }
                            { 1, 1, 0 }
                            { 0.793774486, 0.461956531, 0 }
                            { 0.130434781, 0.295186341, 0 }
                            { 0, 0.244565219, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_AnimeShapes02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLinger: option[f32] = {
                    10.1999998
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "flash1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.214831769, 0.649820685, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.494117647, 1, 0.807843149, 1 }
                            { 0.58431375, 0.764705896, 1, 0 }
                        }
                    }
                }
                pass: i16 = 160
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec3] = {
                            { 1.05434787, 2, 2 }
                            { 2.5, 1.98110485, 1.83087254 }
                            { 0.300000012, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/Morgana_Skin06_BA_Tar_Hot.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                        }
                        values: list[f32] = {
                            3
                            15
                        }
                    }
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
                                    0.200000003
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    0.449999988
                }
                emitterName: string = "W_Cast_Electricity"
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 40
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.800228894, 0.433539331, 1, 1 }
                            { 0.515220881, 0.125276566, 0.980407417, 1 }
                            { 0, 0.301838726, 1, 0.670588255 }
                            { 0, 0.0803387538, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.20000005
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
                            { 126, 0, 0 }
                            { 24.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook_3x3.dds"
                frameRate: f32 = 28
                numFrames: u16 = 9
                startFrame: u16 = 1
                texDiv: vec2 = { 3, 3 }
            }
        }
        particleName: string = "SRU_Dragon_Hextech_BA_Tar"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_BA_Tar"
        soundOnCreateDefault: string = "Play_sfx_SRU_Dragon_Hextech_HextechAttack_hit"
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_IdleAgro_BodyBurst" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
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
                    1
                }
                lifetime: option[f32] = {
                    0.600000024
                }
                emitterName: string = "Electricity_AlwaysOn"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 150
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
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
                            { 0.663233399, 0.180285349, 0.999298096, 1 }
                            { 0, 0.333333343, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
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
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.10000002
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 120, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook.dds"
                frameRate: f32 = 30
                numFrames: u16 = 9
                startFrame: u16 = 6
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                isSingleParticle: flag = true
                emitterName: string = "FloorShockwave"
                importance: u8 = 2
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -113.022003, -50, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.190005347 }
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
                                    0.300000012
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.190005347 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.251442909
                            0.670639873
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 0, 1 }
                            { 0, 0.330006868, 1, 0.310002297 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
                depthBiasFactors: vec2 = { -1, -25 }
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -0.999999821, -8.74316441e-08 }
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
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, -0.999999821, -8.74316441e-08 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00510204071
                            0.396550834
                            1
                        }
                        values: list[vec3] = {
                            { 1.12391305, 0, 0 }
                            { 1.79130435, 0, 0 }
                            { 2.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_Shockwave01_Color.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.400000006
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            15
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.119999997
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
                            0.119999997
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.449999988
                }
                emitterLinger: option[f32] = {}
                emitterName: string = "lightning_RuneWars1"
                importance: u8 = 2
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    radius: f32 = 12
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Emote_SideArc_1.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec4] = {
                            { 0.188235298, 0.266666681, 1, 1 }
                            { 0, 0.531670094, 1, 1 }
                            { 0.349019617, 0.772549033, 1, 0.592156887 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.25
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -99
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 2.5
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
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
                            { 0, 360, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 35, 12 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 12, 35, 12 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1.10000002 }
                            { 1.10000002, 0.600000024, 1.5 }
                            { 1.29999995, 1, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 16
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, 0 }
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
                                    1
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
                texDiv: vec2 = { 4, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
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
                    0.25
                }
                lifetime: option[f32] = {
                    0.349999994
                }
                isSingleParticle: flag = true
                emitterName: string = "Clumps"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
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
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 800, 200 }
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
                                    0.699999988
                                    2
                                }
                            }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 800, 200 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 6, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -350, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -350, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 120
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -55.5645142, -60, 0 }
                }
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
                                    0.800000012
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
                    constantValue: vec4 = { 0.472098887, 0.495857179, 0.647806525, 1 }
                }
                pass: i16 = -8
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 10, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/LeeSin/Skins/Skin31/Particles/LeeSin_Skin31_E_Dirt.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, -1 }
                }
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
                                    0.699999988
                                    1.29999995
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
                    1
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "smoke"
                importance: u8 = 4
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1200, 20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1200, 20, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.349999994
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
                            { 0, -25, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 60
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -55.5645142, -52.8371964, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.639993906, 0.530006886, 0.409994662, 0.300007641 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.340001523 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.556122422
                                1
                            }
                            values: list[f32] = {
                                0
                                0.826086938
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.400000006
                    erosionMapName: string = "ASSETS/Characters/TahmKench/Skins/Base/Particles/TahmKench_Base_Smoke_2_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -50 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -0, 0 }
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
                            { 90, -0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -25, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 65, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
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
                            { 350, 65, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 0.5, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 0.600000024 }
                            { 0.5, 0.5, 1 }
                            { 0.600000024, 0.600000024, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/TahmKench/Skins/Base/Particles/TahmKench_Base_Smoke_2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.479999989
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.364858478, 0.703913927, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.219999999
                            1
                        }
                        values: list[vec4] = {
                            { 0.364858478, 0.703913927, 1, 0 }
                            { 0.364858478, 0.703913927, 1, 1 }
                            { 0.364858478, 0.703913927, 1, 0.200000003 }
                            { 0.364858478, 0.703913927, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.990005314, 0.990005314, 0.990005314, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0599999987
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.200000003
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5500002
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "SpikeShapes"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 450, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 600, 450, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 60, 0, 0 }
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
                        { 0, 1, 0 }
                        { 0, 1, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -60, -52, 0 }
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
                                    0.400000006
                                    0.800000012
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
                    constantValue: vec4 = { 0.678431392, 0.603921592, 0.501960814, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec4] = {
                            { 0.678431392, 0.603921592, 0.501960814, 1 }
                            { 0.678431392, 0.603921592, 0.501960814, 0.500007629 }
                            { 0.678431392, 0.603921592, 0.501960814, 0 }
                        }
                    }
                }
                pass: i16 = 3
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 15
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
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
                                0.800000012
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_GroundBurst.dds"
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 45, 1 }
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
                            { 85, 45, 1 }
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
                            { 0.800000012, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_GroundBurst.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.451999992
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.364858478, 0.703913927, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.219999999
                            1
                        }
                        values: list[vec4] = {
                            { 0.364858478, 0.703913927, 1, 0 }
                            { 0.364858478, 0.703913927, 1, 1 }
                            { 0.364858478, 0.703913927, 1, 0.330006868 }
                            { 0.364858478, 0.703913927, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.990005314, 0.990005314, 0.990005314, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar4"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.223834589, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.103882343, 1, 0 }
                            { 0, 0.183545381, 1, 1 }
                            { 0, 0.223834589, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0.990005314, 0, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar5"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.223834589, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.103882343, 1, 0 }
                            { 0, 0.183545381, 1, 1 }
                            { 0, 0.223834589, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.990005314, 0, 0, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.600000024
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "avatar head"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.223834589, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.103882343, 1, 0 }
                            { 0, 0.183545381, 1, 1 }
                            { 0, 0.223834589, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 0.990005314, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
            }
        }
        particleName: string = "sru_dragon_hextech_Base_Emote_IdleAgro_BodyBurst"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_IdleAgro_BodyBurst"
        overrideScaleCap: option[f32] = {
            -1
        }
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_BodyShine" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.533836901, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.219999999
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.533836901, 1, 0 }
                            { 0, 0.533836901, 1, 1 }
                            { 0, 0.4377487, 1, 0.439993888 }
                            { 0, 0.297420502, 0.993881106, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.990005314, 0.990005314, 0.990005314, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -110, 50, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.269993126 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.280827045, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.119999997
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.280827045, 1, 0 }
                            { 0, 0.280827045, 1, 1 }
                            { 0, 0.230279461, 1, 0.439993888 }
                            { 0, 0.156459242, 0.993881106, 0 }
                        }
                    }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 96, 96 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -110, 100, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 33.4129982, 7.46899986, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.470160991, 0, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.119999997
                            0.300000012
                            0.544217706
                            1
                        }
                        values: list[vec4] = {
                            { 0.470160991, 0, 1, 0 }
                            { 0.470160991, 0, 1, 1 }
                            { 0.253887653, 0, 1, 0.340001523 }
                            { 0.0953029022, 0, 0.9978652, 0.682432413 }
                            { 0.106716171, 0, 0.993881106, 0 }
                        }
                    }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 96, 96 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
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
                            0.349999994
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.349999994
                }
                emitterName: string = "Electricity_AlwaysOn"
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 2
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -81.586998, 100, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.629999995
                            1
                        }
                        values: list[vec4] = {
                            { 0.332799256, 0.855558097, 1, 1 }
                            { 0, 0.333333343, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
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
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
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
                                    1.10000002
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
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook_3x3.dds"
                frameRate: f32 = 28
                numFrames: u16 = 9
                startFrame: u16 = 1
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 35
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.419999987
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.419999987
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        20
                                    }
                                }
                            }
                            axisFraction: vec3 = { 2.10599995, 0.702000022, 2.10599995 }
                        }
                    }
                }
                emitterName: string = "Glow4"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 800, 150, 0 }
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
                            { 800, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 6, 6 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 120, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 120, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -81.586998, 95.3339996, 0 }
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.19047837, 0.408651859, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.19047837, 0.408651859, 1, 1 }
                            { 0.19047837, 0.408651859, 1, 0.170000762 }
                            { 0.19047837, 0.408651859, 1, 0.0899977088 }
                            { 0.19047837, 0.408651859, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.19839026
                            0.361017942
                            0.496447206
                            0.702170551
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 0.423913032, 0 }
                            { 0.12407241, 0.731967747, 0 }
                            { 0.286515862, 0.629096627, 0 }
                            { 0.123710409, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        20
                                    }
                                }
                            }
                            axisFraction: vec3 = { 2.10599995, 0.702000022, 2.10599995 }
                        }
                    }
                }
                emitterName: string = "Glow5"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1000, 350, 0 }
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
                            { 1000, 350, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -350, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -350, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -81.586998, 95.3339996, 0 }
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.460303664, 0.605752647, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.460303664, 0.605752647, 1, 1 }
                            { 0.460303664, 0.605752647, 1, 0.170000762 }
                            { 0.460303664, 0.605752647, 1, 0.0899977088 }
                            { 0.460303664, 0.605752647, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.29280898
                            0.39112246
                            0.530656874
                            0.640593112
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 0.423913032, 0 }
                            { 0.311764717, 0.731967747, 0 }
                            { 0.65882355, 0.629096627, 0 }
                            { 0.452941179, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "sru_dragon_hextech_Base_Emote_BodyShine"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_BodyShine"
        overrideScaleCap: option[f32] = {
            -1
        }
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_BA_Empowered_State" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
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
                    1
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Electricity_AlwaysOn"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 150
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
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
                            { 0.694193959, 0.16562143, 1, 1 }
                            { 0, 0.333333343, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
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
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.10000002
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook.dds"
                frameRate: f32 = 30
                numFrames: u16 = 9
                startFrame: u16 = 6
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.223834589, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.103882343, 1, 0 }
                            { 0, 0.183545381, 1, 1 }
                            { 0, 0.223834589, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0.990005314, 0, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 200, 100 }
                }
                0x563d4a22: embed = ValueVector3 {
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.330006868 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.280827045, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.280827045, 1, 0 }
                            { 0, 0.230279461, 1, 0.439993888 }
                            { 0, 0.157264858, 0.990005314, 1 }
                        }
                    }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 96, 96 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.29999995
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 200, 100 }
                }
                0x563d4a22: embed = ValueVector3 {
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.250003815 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.388662547, 0, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.116666682
                            0.360136062
                            0.619081616
                            0.681870699
                            0.793299317
                            0.873333335
                            1
                        }
                        values: list[vec4] = {
                            { 0.388662547, 0, 1, 0 }
                            { 0.20987837, 0, 1, 0.170000762 }
                            { 0.190443754, 0, 1, 0.887118697 }
                            { 0.171009138, 0, 1, 0.343559325 }
                            { 0.143805429, 0, 0.990005314, 0.886844099 }
                            { 0.128720626, 0, 0.993267775, 0.131323248 }
                            { 0.0893920884, 0, 0.990005314, 0.880596995 }
                            { 0.0893920884, 0, 0.990005314, 1 }
                        }
                    }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 96, 96 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
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
                            0.349999994
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.349999994
                }
                emitterName: string = "Electricity_AlwaysOn1"
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 2
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -81.586998, 100, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.629999995
                            1
                        }
                        values: list[vec4] = {
                            { 0.332799256, 0.855558097, 1, 1 }
                            { 0, 0.333333343, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
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
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
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
                                    1.10000002
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
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook.dds"
                frameRate: f32 = 30
                numFrames: u16 = 9
                startFrame: u16 = 6
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar1"
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
                    constantValue: vec4 = { 1, 1, 1, 0.269993126 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.0500000007
                    fresnelColor: vec4 = { 0, 0.454001665, 1, 0 }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00100005, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_BA_white_RGB.dds"
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.164324403, 0.54052031, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.219999999
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.0396499857, 0.250857204, 1, 0 }
                            { 0.0887354314, 0.382921129, 1, 0.43921569 }
                            { 0.129115075, 0.472203732, 0.988143742, 1 }
                            { 0.164324403, 0.54052031, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.990005314, 0.990005314, 0.990005314, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Ashe_Base_ground_CrackNoise_mult.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 3, 3 }
                    }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0.5, 0 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.5, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 35
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0
                            105
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0.5
                            1
                        }
                        values: list[f32] = {
                            0.349999994
                            0.560000002
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1.20000005
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 50
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        20
                                    }
                                }
                            }
                            axisFraction: vec3 = { 6.31799984, 2.10599995, 6.31799984 }
                        }
                    }
                }
                emitterName: string = "Glow2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 150, 0 }
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
                            { 100, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 6, 6 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 25, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 120
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 350, 100 }
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.542626083, 0.665888429, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.542626083, 0.665888429, 1, 1 }
                            { 0.542626083, 0.665888429, 1, 0.170000762 }
                            { 0.542626083, 0.665888429, 1, 0.0899977088 }
                            { 0.542626083, 0.665888429, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.223775238
                            0.39112246
                            0.530656874
                            0.640593112
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1.62162161, 0.423913032, 0 }
                            { 0.311764717, 0.731967747, 0 }
                            { 0.65882355, 0.629096627, 0 }
                            { 0.452941179, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.223834589, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.103882343, 1, 0 }
                            { 0, 0.183545381, 1, 1 }
                            { 0, 0.223834589, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.990005314, 0, 0, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.600000024
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "avatar head"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.223834589, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.103882343, 1, 0 }
                            { 0, 0.183545381, 1, 1 }
                            { 0, 0.223834589, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_EmissionMask.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_dragon_hextech_basicgradient.dds"
                    PaletteTextureAddressMode: u8 = 2
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 0.990005314, 0 }
                    }
                }
                texAddressModeBase: u8 = 2
            }
        }
        particleName: string = "sru_dragon_hextech_Base_BA_Empowered_State"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_BA_Empowered_State"
        overrideScaleCap: option[f32] = {
            -1
        }
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_BA_Empowered_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    3
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Ground_Glow"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -100, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.420004576 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0649717525
                            0.265536726
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.582391083, 0.349019617, 1, 1 }
                            { 0.0500038154, 0.560006082, 1, 1 }
                            { 0, 0.383993298, 1, 1 }
                            { 0, 0.400503546, 1, 0 }
                        }
                    }
                }
                pass: i16 = 47
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 220, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    11
                }
                isSingleParticle: flag = true
                emitterName: string = "Hit_Small_dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 80, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
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
                    constantValue: vec4 = { 0.0614785999, 0.120286867, 0.264957666, 0.800000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.12785235
                            0.630872488
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 2, 0, 0 }
                            { 1.6692307, 0, 0 }
                            { 0.65882355, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "FloorShockwave"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -100, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.500007629 }
                            { 0.710933089, 0.384313732, 1, 1 }
                            { 0.108186468, 0.445593953, 1, 0.501960814 }
                            { 0.325490206, 0.58431375, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                depthBiasFactors: vec2 = { -1, -25 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.60362661, 0, 0 }
                            { 2.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_Shockwave01_Color.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                    constantValue: vec4 = { 0.385366589, 0.48238346, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.200000003
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.385366589, 0.423740774, 0.513725519, 1 }
                            { 0.288647145, 0.48238346, 0.360784322, 1 }
                            { 0.177268058, 0.36178574, 1, 0.200000003 }
                        }
                    }
                }
                pass: i16 = 151
                miscRenderFlags: u8 = 1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 1.5, 1.5, 1.5 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_Shockwave01_Color.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.419999987
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.419999987
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.600000024
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 50
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        50
                                    }
                                }
                            }
                            axisFraction: vec3 = { 2.10599995, 0.702000022, 2.10599995 }
                        }
                    }
                }
                emitterName: string = "HextechDebris"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 800, 150, 0 }
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
                            { 800, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 6, 6 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 25, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.19047837, 0.408651859, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.19047837, 0.408651859, 1, 1 }
                            { 0.19047837, 0.408651859, 1, 0.170000762 }
                            { 0.19047837, 0.408651859, 1, 0.0899977088 }
                            { 0.19047837, 0.408651859, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.29280898
                            0.39112246
                            0.530656874
                            0.640593112
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 0.423913032, 0 }
                            { 0.311764717, 0.731967747, 0 }
                            { 0.65882355, 0.629096627, 0 }
                            { 0.452941179, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.25
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {}
                emitterName: string = "DirectionalSparks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 900, 0, 0 }
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
                            { 900, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 1, 0.354543388, 0.979446113, 1 }
                            { 0, 0.434500635, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 22, 90, 96 }
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
                            { 22, 90, 96 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.350337088
                            0.496629
                            0.712359428
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 1, 0 }
                            { 0.793774486, 0.461956531, 0 }
                            { 0.130434781, 0.295186341, 0 }
                            { 0, 0.244565219, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_AnimeShapes02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.600000024
                }
                lifetime: option[f32] = {
                    0.600000024
                }
                isSingleParticle: flag = true
                emitterName: string = "Distort"
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_BA_Cas_Distort.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.0500000007
                    normalMapTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_BA_distortion_soundwaves_01.dds"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 200 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1.29999995, 1.29999995 }
                            { 0.800000012, 1, 1 }
                            { 1.26195645, 0.300000012, 0.300000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_BA_white_RGB.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "Floor_DarkGlow"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0500038154, 0.0699931309, 0.149996191, 0.300007641 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -50
                meshRenderFlags: u8 = 0
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                            0.600000024
                        }
                        values: list[f32] = {
                            3
                            15
                        }
                    }
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
                                    0.200000003
                                    0.800000012
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
                    1
                }
                lifetime: option[f32] = {
                    0.600000024
                }
                emitterName: string = "W_Cast_Electricity"
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 40
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.800228894, 0.433539331, 1, 1 }
                            { 0.515220881, 0.125276566, 0.980407417, 1 }
                            { 0, 0.301838726, 1, 0.670588255 }
                            { 0, 0.0803387538, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -120, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -120, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.200000003
                            0.991666675
                        }
                        values: list[vec3] = {
                            { 200, 0, 0 }
                            { 72.2352982, 0, 0 }
                            { 50.1176491, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook_3x3.dds"
                frameRate: f32 = 28
                numFrames: u16 = 9
                startFrame: u16 = 1
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.949999988
                }
                particleLinger: option[f32] = {
                    11
                }
                isSingleParticle: flag = true
                emitterName: string = "Hit_Small_dark1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.289997697 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.634866893, 0.847623408, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.158000007
                            0.266333342
                            0.358333319
                            0.54733336
                            0.716000021
                            0.878666639
                            1
                        }
                        values: list[vec4] = {
                            { 0.217337877, 0, 1, 1 }
                            { 0, 0.512104988, 1, 1 }
                            { 0, 0.5118981, 1, 1 }
                            { 0, 0.302459359, 1, 1 }
                            { 0, 0.304295957, 1, 0.156862751 }
                            { 0, 0.30882284, 1, 0.188235298 }
                            { 0, 0.136892438, 1, 0.0901960805 }
                            { 0, 0.0482563972, 0.33488974, 0 }
                        }
                    }
                }
                pass: i16 = 150
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.103333332
                            0.209205806
                            1
                        }
                        values: list[vec3] = {
                            { 2, 0, 0 }
                            { 0.839818954, 0, 0 }
                            { 0.582352936, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Items/8001/Particles/bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {}
                emitterName: string = "DirectionalSparks_Negative"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 900, 0, 0 }
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
                            { 900, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0686503425, 0.0652628392, 0.146623939, 1 }
                }
                pass: i16 = 80
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 100, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.350337088
                            0.496629
                            0.712359428
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 1, 0 }
                            { 0.793774486, 0.461956531, 0 }
                            { 0.130434781, 0.295186341, 0 }
                            { 0, 0.244565219, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_AnimeShapes02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.219999999
                            0.400000006
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0.0500038154 }
                            { 0, 0, 0, 0.62999922 }
                            { 0, 0, 0, 0.11999695 }
                            { 0, 0, 0, 0.310002297 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 31.5
                    fresnelColor: vec4 = { 0, 0.697169423, 1, 0 }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_BA_white_RGB.dds"
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.0799999982
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0138399331, 0, 0.15643549, 1 }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00199997, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_BA_white_RGB.dds"
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.25
                }
                lifetime: option[f32] = {
                    0.349999994
                }
                emitterName: string = "RandomArcs1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Cylinder.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.190005347 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.308339059, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.308339059, 1, 0 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 0 }
                        }
                    }
                }
                pass: i16 = 99
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
                    erosionFeatherIn: f32 = 0.400000006
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 360, 0.25 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -4
                                    4
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
                            { 25, 360, 0.25 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 12, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 0.75, 0.75 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.20000005
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.20000005
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.75, 0.75, 0.75 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1, 1.20000005 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 1.20000005, 0.300000012, 0.360000014 }
                            { 1.20000005, 1, 1.20000005 }
                            { 1.38, 2, 1.38 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
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
                                    -1
                                    1
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
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                            0.800000012
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                            { 0.100000001, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1.5, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                        }
                        values: list[vec2] = {
                            { 1.5, 1 }
                            { 1.5, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLinger: option[f32] = {
                    10.1999998
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "flash2"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.629663527, 0.214831769, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.494117647, 1, 0.807843149, 1 }
                            { 0.58431375, 0.764705896, 1, 0 }
                        }
                    }
                }
                pass: i16 = 160
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec3] = {
                            { 1.05434787, 2, 2 }
                            { 2.5, 1.98110485, 1.83087254 }
                            { 0.300000012, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/Morgana_Skin06_BA_Tar_Hot.dds"
            }
        }
        particleName: string = "SRU_Dragon_Hextech_BA_Empowered_Tar"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_BA_Empowered_Tar"
        soundOnCreateDefault: string = "Play_sfx_SRU_Dragon_Hextech_HextechAttack_hit"
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_IdleAgro_HeadShaking" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.349999994
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.100000001
                                }
                                keyValues: list[f32] = {
                                    1
                                    0
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            12
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
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
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Electricity_AlwaysOn"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 12
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 29.9339371, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.25
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.743678927, 0.330769807, 1, 1 }
                            { 0, 0.333333343, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.01729906, 0.982396066, 0.999994516 }
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
                        values: list[vec3] = {
                            { 1.01729906, 0.982396066, 0.999994516 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
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
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
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
                            { 40, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook.dds"
                frameRate: f32 = 35
                numFrames: u16 = 9
                startFrame: u16 = 6
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.449999988
                }
                isSingleParticle: flag = true
                period: option[f32] = {
                    0.600000024
                }
                emitterName: string = "Temp_Mesh"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 32.6839981, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.250003815 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.157900363, 0.213244826, 0.653513372, 1 }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.600000024
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.119999997
                            0.300000012
                            0.5
                            0.800000012
                        }
                        values: list[vec3] = {
                            { 1, 1, 1.10000002 }
                            { 2, 2, 1.14999998 }
                            { 0.800000012, 0.800000012, 1.20000005 }
                            { 1.20000005, 1.20000005, 1.20000005 }
                            { 3, 3, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 18
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                uvScale: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                            { 1, 0.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.119999997
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.0799999982
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.449999988
                }
                isSingleParticle: flag = true
                period: option[f32] = {
                    0.600000024
                }
                emitterName: string = "Temp_Mesh3"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 46.5015717, 42.9827118, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.208926529, 0.666819274, 1, 1 }
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 1.79999995 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 10
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                uvScale: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                            { 1, 0.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.449999988
                }
                isSingleParticle: flag = true
                period: option[f32] = {
                    0.600000024
                }
                emitterName: string = "Temp_Mesh4"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 32.6839981, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.449999988
                            0.600000024
                        }
                        values: list[vec4] = {
                            { 0.342412442, 0.989410222, 0.975722909, 1 }
                            { 0.0260929279, 0.348134577, 1, 1 }
                            { 0, 0.0614938587, 1, 0.298039228 }
                        }
                    }
                }
                pass: i16 = 1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.600000024
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.119999997
                            0.300000012
                            0.5
                            0.800000012
                        }
                        values: list[vec3] = {
                            { 1.8369565, 1.78913045, 1.10000002 }
                            { 2, 2, 1.14999998 }
                            { 0.800000012, 0.800000012, 1.20000005 }
                            { 1.20000005, 1.20000005, 1.20000005 }
                            { 3, 3, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 18
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 1, 0.800000012 }
                            { 1, 0.400000006 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.449999988
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Core"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 32.6839981, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.160006106 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.119999997
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.377492934, 0, 1 }
                            { 0, 0.329839021, 1, 0.329411775 }
                            { 0, 0.059998475, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4.5, 4.5, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.119999997
                            0.391836733
                            0.692176878
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1.10000002 }
                            { 2, 2, 1.14999998 }
                            { 1.27826083, 1.27826083, 1.20000005 }
                            { 1.36304355, 1.30869567, 1.20000005 }
                            { 2, 2, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Gradient_Linear_Vertical01.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Gradient_Linear_Vertical04.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Core1"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 46.5015717, 42.9827118, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.313633949, 0.970000744, 0.490196079 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.268027216
                            1
                        }
                        values: list[vec4] = {
                            { 0.579995394, 0.874769211, 1, 0 }
                            { 0.349996179, 0.86999315, 1, 1 }
                            { 0.300007641, 0.60999465, 1, 0.370277911 }
                            { 0.290196091, 0.421149015, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2.5, 2.5, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.121700674
                            0.391836733
                            0.695578218
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1.10000002 }
                            { 1.63586962, 1.63586962, 1.14999998 }
                            { 1.27826083, 1.27826083, 1.20000005 }
                            { 1.30869567, 1.30869567, 1.20000005 }
                            { 1.701087, 1.701087, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Gradient_Linear_Vertical01.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Gradient_Linear_Vertical04.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.680000007
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 15, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 37.1792793, 21.4092751, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.179995418, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.179995418, 1, 1 }
                            { 0, 0.179995418, 1, 0.209994659 }
                            { 0, 0.179995418, 1, 0 }
                        }
                    }
                }
                pass: i16 = 12
                depthBiasFactors: vec2 = { -1, -2 }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 96, 96 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        20
                                    }
                                }
                            }
                            axisFraction: vec3 = { 2.10599995, 0.702000022, 2.10599995 }
                        }
                    }
                }
                emitterName: string = "Glow1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1000, 350, 0 }
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
                            { 1000, 350, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -350, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -350, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 20
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.693369985, 0.460303664, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.693369985, 0.460303664, 1, 1 }
                            { 0.693369985, 0.460303664, 1, 0.170000762 }
                            { 0.693369985, 0.460303664, 1, 0.0899977088 }
                            { 0.693369985, 0.460303664, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.29280898
                            0.39112246
                            0.530656874
                            0.640593112
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 0.423913032, 0 }
                            { 0.311764717, 0.731967747, 0 }
                            { 0.65882355, 0.629096627, 0 }
                            { 0.452941179, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "sru_dragon_hextech_Base_Emote_IdleAgro_HeadShaking"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_IdleAgro_HeadShaking"
        overrideScaleCap: option[f32] = {
            -1
        }
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Death" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    15
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "DeathGeo"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -20, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 35, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/sru_dragon_hextech.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/sru_dragon_hextech.skl"
                        mAnimationName: string = "ASSETS/Characters/SRU_Dragon/Skins/Base/Animations/SRU_Dragon_Death.anm"
                    }
                }
                blendMode: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.300000012 }
                            { 0.600000024, 0.649027228, 0.699992359, 0.0980392173 }
                            { 0.100007631, 0.128938735, 0.200000003, 0 }
                        }
                    }
                }
                pass: i16 = 3
                alphaRef: u8 = 1
                disableBackfaceCull: bool = true
                doesCastShadow: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.25, 1.25, 1.25 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/SRU_Dragon_Hextech_TX_CM.dds"
                uvMode: u8 = 2
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Death_Mult.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.800000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    14
                }
                lifetime: option[f32] = {
                    5.5
                }
                isSingleParticle: flag = true
                emitterName: string = "groundBurn"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
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
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 10, -90 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 10, -90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 380, 380, 0 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Death_groundBurn.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Death_groundBurn_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.0599999987 }
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
                                { 0, 0.0599999987 }
                            }
                        }
                    }
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
                timeBeforeFirstEmission: f32 = 0.800000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    10.6000004
                }
                lifetime: option[f32] = {
                    4.19999981
                }
                emitterName: string = "Flames4x4"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 60, 100 }
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
                                1
                            }
                            values: list[vec3] = {
                                { 50, 60, 100 }
                                { 50, 60, 250 }
                            }
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 1 }
                        }
                    }
                }
                pass: i16 = 8
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
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
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
                            { 100, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 65, 65, 65 }
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
                                    -0.400000006
                                    -1
                                    1
                                    0.400000006
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 65, 65, 65 }
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
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 0.800000012, 1, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Death_Flames_4x4.dds"
                frameRate: f32 = 24
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.800000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
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
                                    0.699999988
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
                    4.5
                }
                emitterName: string = "circleburn"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -50 }
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
                                    0.300000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, -50 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 100 }
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
                                { 0, 0, 100 }
                            }
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.300000012, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.300000012, 0, 0, 0 }
                            { 0.300000012, 0, 0, 1 }
                            { 0.300000012, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 6
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
                                    1
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
                    constantValue: vec3 = { 320, 320, 0 }
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
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_BA1_GroundDirt.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
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
                                    0.200000003
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
                    0.200000003
                }
                emitterName: string = "Rays"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 500 }
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 500 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 100 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.800000012
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1
                                        0.300000012
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 100 }
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
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.20242618, 0.742244601, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.20242618, 0.742244601, 1, 0 }
                            { 0.20242618, 0.742244601, 1, 1 }
                            { 0.076281637, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 18
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 160, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 160, 0 }
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
                            { 0, 0, 0 }
                            { 1, 3, 0 }
                            { 0.400000006, 0.100000001, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Death_Rays.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                                    0.5
                                    1
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
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Smoke"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 400, 0 }
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
                            { 400, 400, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 4, 4 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 60, 0, 0 }
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
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.300007641, 0.761303127, 1, 1 }
                            { 0, 0, 0, 0.300000012 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 20
                isDirectionOriented: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 220, 220, 200 }
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
                                    1.5
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 220, 220, 200 }
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
                            { 0.600000024, 0.100000001, 0.600000024 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/FB_explosion_smoke.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ground_CrackNoise_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.300000012 }
                    }
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
                                        1
                                        0
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        0
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
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "CenterFlare"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.622995317, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 1, 1 }
                            { 0, 0.622995317, 1, 1 }
                            { 0, 0.622995317, 1, 1 }
                        }
                    }
                }
                pass: i16 = 5
                miscRenderFlags: u8 = 1
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
                            { 1, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1780, 1780, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.300000012, 0.300000012, 0.300000012 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Dragon_ChemTech/skins/base/Particles/sru_dragon_chemtech_Base_Glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0799999982
                rate: embed = ValueFloat {
                    constantValue: f32 = 120
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
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
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "Sparkflare"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.100000001
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
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 0, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
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
                            { 0, 50, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 130 }
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
                                        0.5
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 130 }
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
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.187563896, 0.658777773, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 34
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
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 320, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
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
                            { 35, 320, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 0 }
                            { 0.100000001, 0.100000001, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/SRU_Dragon_ChemTech/skins/base/Particles/sru_dragon_chemtech_Base_Glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.699999988
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0.300000012
                            0.600000024
                        }
                        values: list[f32] = {
                            6
                            30
                        }
                    }
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
                                    0.200000003
                                    0.800000012
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
                    1
                }
                lifetime: option[f32] = {
                    3
                }
                emitterName: string = "W_Cast_Electricity"
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 40
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.800228894, 0.433539331, 1, 1 }
                            { 0.125276566, 0.650614202, 0.980407417, 1 }
                            { 0, 0.301838726, 1, 0.670588255 }
                            { 0, 0.0803387538, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0.927999973, 1 }
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
                        values: list[vec3] = {
                            { 1, 0.927999973, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -120, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -120, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.200000003
                            0.991666675
                        }
                        values: list[vec3] = {
                            { 200, 0, 0 }
                            { 72.2352982, 0, 0 }
                            { 50.1176491, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook_3x3.dds"
                frameRate: f32 = 28
                numFrames: u16 = 9
                startFrame: u16 = 1
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.600000024
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Add_Wave"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
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
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -13.0765305, -9.39466095, 37.4409943 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_DragonPit_DragonGroundShapes.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/SR/common_alpha_21.dds"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.119999997
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.059998475, 1, 0 }
                            { 0, 0.529335499, 1, 1 }
                            { 0.0295109488, 0.396841377, 1, 1 }
                            { 0.557335794, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = -1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.25, 1.20000005, 0.800000012 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_DragonPitBase_01.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 0 }
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
                            { 2, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 4, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 4, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_DragonPitBase_01_Guide.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.25 }
                    }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { -0.5, 0 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec2] = {
                                { -0.5, 0 }
                                { -0.150000006, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.10000002
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterName: string = "AroundLightning"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 18.9953461, 10, 50.3961182 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_DragonPit_AroundCylinder_Lightning_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.643503487, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.680000007
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.643503487, 1, 1 }
                            { 0, 0.614880443, 1, 1 }
                            { 0, 0.303630352, 1, 1 }
                            { 0, 0.0257362109, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -179.999985, 44.9999924, -179.999908 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.300000012, 0.5, 0.800000012 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.5, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 12
                numFrames: u16 = 4
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
                                    1
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
                texDiv: vec2 = { 4, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -0.449999988 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.75
                        }
                        values: list[vec2] = {
                            { 0, -0.449999988 }
                            { 0, -0.0225000009 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.300000012 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.79999995
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.319999993
                }
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterName: string = "AroundLightning1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 18.9953461, 10, 50.3961182 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_DragonPit_AroundCylinder_Lightning_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.643503487, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.680000007
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.643503487, 1, 1 }
                            { 0, 0.614880443, 1, 1 }
                            { 0, 0.303630352, 1, 1 }
                            { 0, 0.0257362109, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -180, 280, -180 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.300000012, 0.5, 0.800000012 }
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.5, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 12
                numFrames: u16 = 4
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
                                    1
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
                texDiv: vec2 = { 4, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -0.449999988 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.75
                        }
                        values: list[vec2] = {
                            { 0, -0.449999988 }
                            { 0, -0.0225000009 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.300000012 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
        }
        particleName: string = "sru_dragon_hextech_Base_Death"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Death"
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_WingsFX_02" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.39999998
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
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.119999997
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.119999997
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Charged_Beam_Core2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -8.46441269, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh_Offset.scb"
                    }
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.438498527, 0.826215029, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.348316431, 0.410768867, 1, 1 }
                            { 0.0457869135, 0.376817584, 1, 1 }
                            { 0.0219265986, 0.0578293763, 0.229999244, 0 }
                        }
                    }
                }
                pass: i16 = 25
                softParticleParams: pointer = VfxSoftParticleDefinitionData {}
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 800, 500, 500 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 2
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 2 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.400000006 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Charged_Beam_Core3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -8.46441269, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh_Offset.scb"
                    }
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.469993144 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0200045779, 0.130006865, 0.269993126, 0.360006094 }
                }
                pass: i16 = 20
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1200, 120, 800 }
                }
                texture: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Charged_Beam_Base"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.229999244 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.556450725, 0.100007631, 1, 0.470588237 }
                }
                pass: i16 = 25
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.0583333336
                            0.257954419
                            0.744106889
                            1
                        }
                        values: list[vec3] = {
                            { 4, 0, 0 }
                            { 3.24705887, 0, 0 }
                            { 2.38398194, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
        }
        particleName: string = "sru_dragon_hextech_Base_Emote_WingsFX_02"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_WingsFX_02"
        overrideScaleCap: option[f32] = {
            -1
        }
        transform: mtx44 = {
            0.99999994, 0, 0, 0
            0, 0.99999994, 0, 0
            0, 0, 0.999999881, 0
            0, 0, 0, 1
        }
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_BA_Charge" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.100000001
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.25
                }
                lifetime: option[f32] = {
                    0.899999976
                }
                emitterName: string = "RandomArcs"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -50, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
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
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_BA_LightningMesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.308339059, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.300000012
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 0 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 0 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 1 }
                        }
                    }
                }
                pass: i16 = 99
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
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 360, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.26836735
                            0.381292522
                            0.521428585
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 0.971467376, 1 }
                            { 1, 0.498641312, 1 }
                            { 1, 0.756793499, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                numFrames: u16 = 4
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
                                    -1
                                    1
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
                texDiv: vec2 = { 4, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0
                            36
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                emitterName: string = "glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 1, 1, 1 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.158000007
                            1
                        }
                        values: list[vec4] = {
                            { 0.340001523, 0, 1, 0 }
                            { 0, 0.600000024, 1, 0.409994662 }
                            { 0.978286386, 0.271976799, 1, 1 }
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
                            { 1, 1, 1, 0.140001521 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 10
                }
                isUniformScale: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    -0.5
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 80, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.315306127
                            1
                        }
                        values: list[vec3] = {
                            { 1.5, 0, 0 }
                            { 0.699999988, 1.5, 0 }
                            { 0.5, 1.5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/LeeSin/Skins/Skin31/Particles/LeeSin_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waves_B"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Mouth.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.108842604, 0.471396953, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.150377661, 0.450720996, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
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
                    constantValue: vec3 = { 1.60000002, 2, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.994897962
                        }
                        values: list[vec3] = {
                            { 1.4281081, 1, 1 }
                            { 1.5, 0, 0 }
                            { 0.486486465, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.800000012, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    11
                }
                isSingleParticle: flag = true
                emitterName: string = "Hit_Small_dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.2399939 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.158000007
                            0.248000011
                            0.387588978
                            0.54733336
                            0.716000021
                            0.878666639
                            1
                        }
                        values: list[vec4] = {
                            { 0.340001523, 0, 1, 0 }
                            { 0, 0.600000024, 1, 0.749996185 }
                            { 0.707164109, 0, 1, 0.639215708 }
                            { 0, 0.600000024, 1, 0.624124527 }
                            { 0.507331967, 0, 1, 0.592156887 }
                            { 0, 0.360006094, 1, 0.52031827 }
                            { 0.635492504, 0, 1, 0.909803927 }
                            { 0.521660209, 0, 1, 1 }
                        }
                    }
                }
                pass: i16 = 150
                alphaRef: u8 = 1
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                depthBiasFactors: vec2 = { -1, -1 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 98, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.209205806
                            0.644949555
                            0.78018868
                            1
                        }
                        values: list[vec3] = {
                            { 1.54999995, 0, 0 }
                            { 1.31540537, 0, 0 }
                            { 0.592140138, 0, 0 }
                            { 0.54883945, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Items/8001/Particles/bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 35
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.349999994
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        20
                                    }
                                }
                            }
                            axisFraction: vec3 = { 2.10599995, 0.702000022, 2.10599995 }
                        }
                    }
                }
                emitterName: string = "Glow1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 150, 0 }
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
                            { 100, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 6, 6 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 25, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.19047837, 0.408651859, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.19047837, 0.408651859, 1, 1 }
                            { 0.19047837, 0.408651859, 1, 0.170000762 }
                            { 0.19047837, 0.408651859, 1, 0.0899977088 }
                            { 0.19047837, 0.408651859, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.29280898
                            0.39112246
                            0.530656874
                            0.640593112
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 3, 0.423913032, 0 }
                            { 0.311764717, 0.731967747, 0 }
                            { 0.65882355, 0.629096627, 0 }
                            { 0.452941179, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waves_B1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Mouth.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.108842604, 0.471396953, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.150377661, 0.450720996, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 180 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 180 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.60000002, 2, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.994897962
                        }
                        values: list[vec3] = {
                            { 1.4281081, 1, 1 }
                            { 1.5, 0, 0 }
                            { 0.486486465, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.800000012, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.600000024, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.35000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waves_B2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Mouth.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.144380867, 0.0150148775, 1, 0.31764707 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.150377661, 0.450720996, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 35, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, -1.5, 1.5 }
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
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.5, -1.5, 1.5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.284693897
                            0.994897962
                        }
                        values: list[vec3] = {
                            { 1.48648643, 1.39999998, 1.39999998 }
                            { 1.5, 1.5, 1.5 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
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
                            { 1, 0 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { -0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { -1, 0 }
                            { -0.5, 0 }
                            { -0.150000006, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.35599995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waves_B3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Mouth.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.140001521, 0.0200045779, 1, 0.530006886 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.150377661, 0.450720996, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 180 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 180 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -35, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
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
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.284693897
                            0.994897962
                        }
                        values: list[vec3] = {
                            { 1.48648643, 1.39999998, 1.39999998 }
                            { 1.5, 1.5, 1.5 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
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
                            { 1, 0 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { -0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { -1, 0 }
                            { -0.5, 0 }
                            { -0.150000006, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                        }
                        values: list[f32] = {
                            3
                            15
                        }
                    }
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
                                    0.200000003
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    0.600000024
                }
                emitterName: string = "W_Cast_Electricity2"
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 40
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.800228894, 0.433539331, 1, 1 }
                            { 0.515220881, 0.125276566, 0.980407417, 1 }
                            { 0, 0.301838726, 1, 0.670588255 }
                            { 0, 0.0803387538, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.20000005
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
                            { 45, 0, 0 }
                            { 8.75, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook_3x3.dds"
                frameRate: f32 = 28
                numFrames: u16 = 9
                startFrame: u16 = 1
                texDiv: vec2 = { 3, 3 }
            }
        }
        particleName: string = "sru_dragon_hextech_Base_BA_Charge"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_BA_Charge"
        soundOnCreateDefault: string = "Play_sfx_SRU_Dragon_Hextech_HextechAttack_cast"
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_Base_BA_Beam" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Lightning"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 800, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.349999994
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.770916283, 0.628717482, 1, 1 }
                            { 0.598001063, 0, 1, 1 }
                            { 0, 0.450827807, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.726950288
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.13639456
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.800000012, 1, 0.5 }
                            { 0, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 4
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.449999988, 0 }
                }
                texDiv: vec2 = { 4, 1 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Lightning1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 600, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.643503487, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.643503487, 1, 1 }
                            { 0, 0.614880443, 1, 1 }
                            { 0, 0.512573838, 1, 1 }
                            { 0, 0.0285248738, 1, 1 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00510204071
                            0.0979762524
                            0.270169973
                            0.462075323
                            0.996616006
                        }
                        values: list[vec3] = {
                            { 0.494565219, 1, 0 }
                            { 1.93984962, 1, 1 }
                            { 0.71318078, 1, 1 }
                            { 1.07535148, 1, 1 }
                            { 1.52778852, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 4
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { -6, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                        }
                        values: list[vec2] = {
                            { -6, 0 }
                            { -0, 0 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.119999997
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.280000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Lightning2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 400, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0948195606, 0.461722732, 1, 1 }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.600000024
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 18, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00510204071
                            0.134693876
                            0.40646258
                            1
                        }
                        values: list[vec3] = {
                            { 0.494565219, 1, 0 }
                            { 1.30978262, 1, 1 }
                            { 2.15760875, 1, 1 }
                            { 2.3641305, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 4
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.200000003, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { -0.200000003, 0 }
                            { -0, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 1 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_GroundBurst.dds"
                    texDivMult: vec2 = { 4, 1 }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -3 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, -3 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
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
                                        1
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
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Lightning3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 800, 0 }
                        }
                        mAnimatedColorWithDistance: embed = ValueColor {
                            constantValue: vec4 = { 1, 0, 0, 1 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.11999695, 0.439993888, 0.360006094 }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 6
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_GroundBurst.dds"
                    texDivMult: vec2 = { 4, 1 }
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                    }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 3 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 3 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
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
                                        1
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
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Base"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 500, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.420004576 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.41115436, 0, 0.547722578, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.41115436, 0, 0.317676574, 0 }
                            { 0.0524929948, 0, 0.547722578, 1 }
                            { 0, 0, 0.203326389, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.119623654
                            0.911290348
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.07865167, 0, 0 }
                            { 1.5, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_Mult01.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.889999986, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.889999986, 0 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Base1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.400671393, 0, 1, 1 }
                            { 0.0233005267, 0.164461732, 0.624414444, 0.772549033 }
                            { 0, 0.0259861145, 0.371221483, 0 }
                        }
                    }
                }
                pass: i16 = 25
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.20125629
                            0.40448761
                            1
                        }
                        values: list[vec3] = {
                            { 0.823369563, 0, 0 }
                            { 1.33136904, 0, 0 }
                            { 1.46739125, 0, 0 }
                            { 0.758152187, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Base2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.250980407, 0.579430819, 1, 1 }
                }
                pass: i16 = 25
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 1, 1 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ProjectileBeam.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -4.5, 0 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
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
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {}
                emitterName: string = "Glow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 150, 0 }
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
                            { 500, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 6, 6 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 25, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.217502102, 0, 1, 1 }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 24, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.29280898
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 0.423913032, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Items/8001/Particles/Evelynn_Base_R_Illaoi_Base_Tentacle_Nidalee_Glowspecks.dds"
            }
        }
        particleName: string = "SRU_Dragon_Hextech_Base_BA_Beam"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_Base_BA_Beam"
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_WingsFX" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Lightning"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh_Curved.scb"
                    }
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 100, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.377660781, 0, 1, 1 }
                }
                pass: i16 = 15
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.600000024
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.333333343
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 4.20652151, 1, 1 }
                            { 6, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 3
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.200000003 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_GroundBurst.dds"
                    texDivMult: vec2 = { 4, 1 }
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                    }
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 2 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 2 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
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
                                        1
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
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.219999999
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Core"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh_Curved.scb"
                    }
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.0699931309 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.004715038, 0, 0.314839393, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.004715038, 0, 0.182605401, 0 }
                            { 0.004715038, 0, 0.110192589, 0.500007629 }
                            { 0.00443214271, 0, 0.173160478, 1 }
                            { 0.00269959029, 0, 0.091365166, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.333333343
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 4.20652151, 1, 1 }
                            { 6, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Lightning1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 7.82505798 }
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh_Curved.scb"
                    }
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 100, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.349999994
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.483146399, 0.963668287, 0.8827039, 1 }
                            { 0, 0.330998689, 1, 1 }
                        }
                    }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.600000024
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 0, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00510204071
                            0.17176871
                            0.494897962
                            1
                        }
                        values: list[vec3] = {
                            { 0.0652173907, 1, 1 }
                            { 1.79347825, 1, 1 }
                            { 7, 1, 1 }
                            { 8, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 3
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.200000003 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Core2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -8.46441269, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_ArcMesh_Offset.scb"
                    }
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.478507668, 0.157289997, 1, 1 }
                            { 0.104417488, 0.45607692, 1, 1 }
                            { 0.0500038154, 0.0699931309, 0.229999244, 0 }
                        }
                    }
                }
                pass: i16 = 25
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 800, 500, 500 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                frameRate: f32 = 2
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.200000003 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.600000024 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Gradient_Linear_Vertical04.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Charged_Beam_Base"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 200, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.379995435 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.10391394, 0.378713667, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.0612400137, 0, 1, 1 }
                            { 0.10391394, 0.378713667, 1, 1 }
                            { 0.10391394, 0.378713667, 1, 0 }
                        }
                    }
                }
                pass: i16 = 25
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.0583333336
                            0.257954419
                            0.558211505
                            1
                        }
                        values: list[vec3] = {
                            { 4, 0, 0 }
                            { 3.24705887, 0, 0 }
                            { 1.54705882, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Hextech_Linear_Vertical.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
        }
        particleName: string = "sru_dragon_hextech_Base_Emote_WingsFX"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_WingsFX"
        overrideScaleCap: option[f32] = {
            -1
        }
        transform: mtx44 = {
            0.99999994, 0, 0, 0
            0, 0.99999994, 0, 0
            0, 0, 0.999999881, 0
            0, 0, 0, 1
        }
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_GemShine" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.269993126 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.518928826, 0.654032171, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.518928826, 0.654032171, 1, 0 }
                            { 0.518928826, 0.654032171, 1, 0.719996929 }
                            { 0.280222356, 0.536309421, 1, 0.930006862 }
                            { 0.337479919, 0, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 96, 96 }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.319999993
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.147896439
                            0.400000006
                            0.587907016
                            0.676375389
                            0.797734618
                            0.833333313
                            1
                        }
                        values: list[vec4] = {
                            { 0.0824139789, 0, 0.162600145, 0 }
                            { 0.674830258, 0, 1, 0.521568656 }
                            { 0.139848933, 0.663401246, 1, 0.960784316 }
                            { 0.194323644, 0.44274053, 1, 0.388235301 }
                            { 0.734035254, 0.280537128, 1, 0.909803927 }
                            { 0.147402152, 0.174547955, 1, 0.333333343 }
                            { 0.900129676, 0.516380548, 1, 1 }
                            { 0.120256349, 0.455436021, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 96, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.150000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 3, 0, 0 }
                            { 1, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 22
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        20
                                    }
                                }
                            }
                            axisFraction: vec3 = { 2.10599995, 0.702000022, 2.10599995 }
                        }
                    }
                }
                emitterName: string = "Glow4"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 800, 150, 0 }
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
                            { 800, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 6, 6 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 25, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 20
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.19047837, 0.408651859, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.19047837, 0.408651859, 1, 1 }
                            { 0.19047837, 0.408651859, 1, 0.170000762 }
                            { 0.19047837, 0.408651859, 1, 0.0899977088 }
                            { 0.19047837, 0.408651859, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.29280898
                            0.39112246
                            0.530656874
                            0.640593112
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 0.423913032, 0 }
                            { 0.311764717, 0.731967747, 0 }
                            { 0.65882355, 0.629096627, 0 }
                            { 0.452941179, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.379999995
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        20
                                    }
                                }
                            }
                            axisFraction: vec3 = { 2.10599995, 0.702000022, 2.10599995 }
                        }
                    }
                }
                emitterName: string = "Glow5"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1000, 350, 0 }
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
                            { 1000, 350, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -350, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -350, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 20
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.460303664, 0.605752647, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.460303664, 0.605752647, 1, 1 }
                            { 0.460303664, 0.605752647, 1, 0.170000762 }
                            { 0.460303664, 0.605752647, 1, 0.0899977088 }
                            { 0.460303664, 0.605752647, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.29280898
                            0.39112246
                            0.530656874
                            0.640593112
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 1, 0.423913032, 0 }
                            { 0.311764717, 0.731967747, 0 }
                            { 0.65882355, 0.629096627, 0 }
                            { 0.452941179, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "sru_dragon_hextech_Base_Emote_GemShine"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_GemShine"
        overrideScaleCap: option[f32] = {
            -1
        }
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_BA_Empowered_Charge" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.100000001
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.25
                }
                lifetime: option[f32] = {
                    0.899999976
                }
                emitterName: string = "RandomArcs"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -50, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
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
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_BA_LightningMesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.308339059, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.300000012
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 0 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 0 }
                            { 0, 0.308339059, 1, 1 }
                            { 0, 0.308339059, 1, 1 }
                        }
                    }
                }
                pass: i16 = 99
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
                    erosionMapName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 360, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.26836735
                            0.381292522
                            0.521428585
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 0.971467376, 1 }
                            { 1, 0.498641312, 1 }
                            { 1, 0.756793499, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_LightningWave_Sheet.dds"
                numFrames: u16 = 4
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
                                    -1
                                    1
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
                texDiv: vec2 = { 4, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Beam_Mask.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                        }
                        values: list[f32] = {
                            3
                            15
                        }
                    }
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
                                    0.200000003
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    0.600000024
                }
                emitterName: string = "W_Cast_Electricity"
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 40
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.800228894, 0.433539331, 1, 1 }
                            { 0.515220881, 0.125276566, 0.980407417, 1 }
                            { 0, 0.301838726, 1, 0.670588255 }
                            { 0, 0.0803387538, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
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
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.20000005
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
                            { 45, 0, 0 }
                            { 8.75, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_Lightning_flipbook_3x3.dds"
                frameRate: f32 = 28
                numFrames: u16 = 9
                startFrame: u16 = 1
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0
                            36
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                emitterName: string = "glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 1, 1, 1 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.525505483, 1, 1 }
                            { 0, 0.720332623, 1, 1 }
                            { 1, 0.257099271, 0.886457622, 1 }
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
                            { 1, 1, 1, 0.140001521 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 10
                }
                isUniformScale: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    -0.5
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 65, 80, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.315306127
                            1
                        }
                        values: list[vec3] = {
                            { 1.5, 0, 0 }
                            { 0.699999988, 1.5, 0 }
                            { 0.5, 1.5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/LeeSin/Skins/Skin31/Particles/LeeSin_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waves_B"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Mouth.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.108842604, 0.471396953, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.150377661, 0.450720996, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
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
                    constantValue: vec3 = { 1.60000002, 2, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.994897962
                        }
                        values: list[vec3] = {
                            { 1.4281081, 1, 1 }
                            { 1.5, 0, 0 }
                            { 0.486486465, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.800000012, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.800000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Hit_Small_dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
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
                            0.158000007
                            0.248000011
                            0.418333322
                            0.54733336
                            0.716000021
                            0.878666639
                            1
                        }
                        values: list[vec4] = {
                            { 0.340001523, 0, 1, 0 }
                            { 0, 0.600000024, 1, 0.749996185 }
                            { 0.707164109, 0, 1, 0.639215708 }
                            { 0, 0.600000024, 1, 0.330006868 }
                            { 0.507331967, 0, 1, 0.592156887 }
                            { 0, 0.360006094, 1, 0.330006868 }
                            { 0.635492504, 0, 1, 0.909803927 }
                            { 0.521660209, 0, 1, 1 }
                        }
                    }
                }
                pass: i16 = 150
                alphaRef: u8 = 1
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                depthBiasFactors: vec2 = { -1, -1 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 98, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.209205806
                            0.606561482
                            0.773790658
                            0.997440815
                        }
                        values: list[vec3] = {
                            { 1.54999995, 0, 0 }
                            { 1.05786693, 0, 0 }
                            { 1.46014011, 0, 0 }
                            { 1.54083943, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Items/8001/Particles/bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 35
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.349999994
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterLinger: option[f32] = {}
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        20
                                    }
                                }
                            }
                            axisFraction: vec3 = { 2.10599995, 0.702000022, 2.10599995 }
                        }
                    }
                }
                emitterName: string = "Glow1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 150, 0 }
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
                            { 100, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 6, 6 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 25, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                particleColorTexture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_SparksRandomRamp.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.19047837, 0.408651859, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.319999993
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.19047837, 0.408651859, 1, 1 }
                            { 0.19047837, 0.408651859, 1, 0.170000762 }
                            { 0.19047837, 0.408651859, 1, 0.0899977088 }
                            { 0.19047837, 0.408651859, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeX: u8 = 3
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 50, 96 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.29280898
                            0.39112246
                            0.530656874
                            0.640593112
                            0.914024234
                            1
                        }
                        values: list[vec3] = {
                            { 0.831521749, 1, 0 }
                            { 3, 0.423913032, 0 }
                            { 0.311764717, 0.731967747, 0 }
                            { 0.65882355, 0.629096627, 0 }
                            { 0.452941179, 0.504464269, 0 }
                            { 0.264705896, 0.12067575, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_HextechSparks.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waves_B1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Mouth.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.108842604, 0.471396953, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.150377661, 0.450720996, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 180 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 180 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.60000002, 2, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.994897962
                        }
                        values: list[vec3] = {
                            { 1.4281081, 1, 1 }
                            { 1.5, 0, 0 }
                            { 0.486486465, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.800000012, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.600000024, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.35000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waves_B2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Mouth.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.144380867, 0.0150148775, 1, 0.31764707 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.150377661, 0.450720996, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 35, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, -2, 1.5 }
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
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, -2, 1.5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.284693897
                            0.994897962
                        }
                        values: list[vec3] = {
                            { 1.48648643, 1.39999998, 1.39999998 }
                            { 1.5, 1.5, 1.5 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
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
                            { 1, 0 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { -0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { -1, 0 }
                            { -0.5, 0 }
                            { -0.150000006, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.35599995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waves_B3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Base_Mouth.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.140001521, 0.0200045779, 1, 0.530006886 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.150377661, 0.450720996, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 180 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 180 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -35, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 2, 1.5 }
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
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 2, 1.5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.284693897
                            0.994897962
                        }
                        values: list[vec3] = {
                            { 1.48648643, 1.39999998, 1.39999998 }
                            { 1.5, 1.5, 1.5 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/SRU_Dragon_Hextech_Trail.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
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
                            { 1, 0 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { -0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { -1, 0 }
                            { -0.5, 0 }
                            { -0.150000006, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 85
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0
                            255
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.25
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.5
                }
                emitterLinger: option[f32] = {}
                emitterName: string = "DirectionalSparks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 0, 0 }
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
                            { 350, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 3
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.400000006
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.354543388, 0.703196764, 1, 1 }
                            { 0, 0.434500635, 1, 1 }
                        }
                    }
                }
                pass: i16 = 12
                alphaRef: u8 = 1
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -25
                                    25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 0, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 22, 100, 96 }
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
                            { 22, 100, 96 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.154336736
                            0.350337088
                            0.496629
                            0.712359428
                            1
                        }
                        values: list[vec3] = {
                            { 0.539999962, 0.0117647061, 0 }
                            { 0.600000024, 1, 0 }
                            { 0.476264685, 0.461956531, 0 }
                            { 0.0782608688, 0.295186341, 0 }
                            { 0, 0.244565219, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/sru_dragon_hextech/Skins/Base/Particles/sru_dragon_hextech_Base_BA_AnimeShapes02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "sru_dragon_hextech_Base_BA_Empowered_Charge"
        particlePath: string = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_BA_Empowered_Charge"
    }
    "Characters/sru_dragon_hextech/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            0xd757c29c = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_BA_Empowered_State"
            0x62e86c1f = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_Base_BA_Beam"
            0xa9b20264 = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_Base_BA_Empowered_Beam"
            "SRU_Dragon_Hextech_BA_Tar" = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_BA_Tar"
            "SRU_Dragon_Hextech_BA_Empowered_Tar" = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/SRU_Dragon_Hextech_BA_Empowered_Tar"
            0x01b978ac = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_BA_Charge"
            0x4e22682b = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_WingsFX"
            0x0bb13012 = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_IdleAgro_HeadShaking"
            0xe9a65147 = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_IdleAgro_BodyBurst"
            0x989eba3e = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_BodyShine"
            0x6d16d45b = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_BA_Empowered_Charge"
            0x757dab42 = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_WingsFX_02"
            0x0727a935 = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Emote_GemShine"
            0x5c42ecbc = "Characters/sru_dragon_hextech/Skins/Skin0/Particles/sru_dragon_hextech_Base_Death"
        }
    }
}
