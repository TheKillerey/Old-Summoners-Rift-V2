#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Turret/Animations/Skin2" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "State2" = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideBase" = SubmeshVisibilityEventData {
                        mName: hash = "HideBase"
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                    }
                    0x3cefb411 = SubmeshVisibilityEventData {
                        mName: hash = 0x3cefb411
                        mShowSubmeshList: list[hash] = {
                            "Stage1"
                        }
                    }
                    0x159a6826 = SubmeshVisibilityEventData {
                        mName: hash = 0x159a6826
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1.anm"
                }
            }
            "State3" = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideBase" = SubmeshVisibilityEventData {
                        mName: hash = "HideBase"
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                    }
                    0xd87f9f9c = SubmeshVisibilityEventData {
                        mName: hash = 0xd87f9f9c
                        mHideSubmeshList: list[hash] = {
                            "Stage1"
                        }
                    }
                    0x39efaf58 = SubmeshVisibilityEventData {
                        mName: hash = 0x39efaf58
                        mShowSubmeshList: list[hash] = {
                            "Stage2"
                        }
                    }
                    0x159a6826 = SubmeshVisibilityEventData {
                        mName: hash = 0x159a6826
                        mHideSubmeshList: list[hash] = {
                            "Cloth1"
                        }
                    }
                    0x149a6693 = SubmeshVisibilityEventData {
                        mName: hash = 0x149a6693
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1.anm"
                }
            }
            "Destroyed" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x07030a82 = SubmeshVisibilityEventData {
                        mName: hash = 0x07030a82
                        mShowSubmeshList: list[hash] = {
                            "Rubble"
                        }
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mName: hash = "HideBase"
                        mHideSubmeshList: list[hash] = {
                            "Base"
                        }
                    }
                    0xd87f9f9c = SubmeshVisibilityEventData {
                        mName: hash = 0xd87f9f9c
                        mHideSubmeshList: list[hash] = {
                            "Stage1"
                        }
                    }
                    0xdb7fa455 = SubmeshVisibilityEventData {
                        mName: hash = 0xdb7fa455
                        mHideSubmeshList: list[hash] = {
                            "Stage2"
                        }
                    }
                    0x6d4f2733 = SubmeshVisibilityEventData {
                        mName: hash = 0x6d4f2733
                        mHideSubmeshList: list[hash] = {
                            "Cloth1"
                        }
                    }
                    0x149a6693 = SubmeshVisibilityEventData {
                        mName: hash = 0x149a6693
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1.anm"
                }
            }
            0x2e246d03 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "cloth"
                mTrackDataName: hash = "cloth"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1.anm"
                }
            }
            0xaa006aba = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Destroyed"
                }
            }
            0xfd86c944 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "cloth"
                mTrackDataName: hash = "cloth"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1.anm"
                }
            }
            0xcc2030a0 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break1" = ParticleEventData {
                        mName: hash = "Break1"
                        mEffectKey: hash = "SRU_ChaosTurret1_break1"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Root_break"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mName: hash = "HideBase"
                        mStartFrame: f32 = 1
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                    }
                    0x3cefb411 = SubmeshVisibilityEventData {
                        mName: hash = 0x3cefb411
                        mStartFrame: f32 = 1
                        mShowSubmeshList: list[hash] = {
                            "Stage1"
                        }
                    }
                    0x6d4f2733 = SubmeshVisibilityEventData {
                        mName: hash = 0x6d4f2733
                        mStartFrame: f32 = 1
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1_seq.anm"
                }
            }
            0xf5c65fef = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break2" = ParticleEventData {
                        mName: hash = "Break2"
                        mEffectKey: hash = "SRU_ChaosTurret1_break2"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Root_break"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mName: hash = "HideBase"
                        mHideSubmeshList: list[hash] = {
                            "SRUAP_ChaosTurret1_Mat"
                        }
                    }
                    0x3cefb411 = SubmeshVisibilityEventData {
                        mName: hash = 0x3cefb411
                        mShowSubmeshList: list[hash] = {
                            "Stage2"
                        }
                        mHideSubmeshList: list[hash] = {
                            "Stage1"
                        }
                    }
                    0x6d4f2733 = SubmeshVisibilityEventData {
                        mName: hash = 0x6d4f2733
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                    }
                    0x149a6693 = SubmeshVisibilityEventData {
                        mName: hash = 0x149a6693
                        mHideSubmeshList: list[hash] = {
                            "Cloth1"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1_seq.anm"
                }
            }
            "Destroyed_seq" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Break3" = ParticleEventData {
                        mName: hash = "Break3"
                        mEffectKey: hash = "SRU_ChaosTurret1_break3"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Root_break"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                        mIsDetachable: bool = true
                    }
                    "HideBase" = SubmeshVisibilityEventData {
                        mName: hash = "HideBase"
                        mHideSubmeshList: list[hash] = {
                            "Base"
                        }
                    }
                    0xd87f9f9c = SubmeshVisibilityEventData {
                        mName: hash = 0xd87f9f9c
                        mShowSubmeshList: list[hash] = {
                            "Stage2"
                        }
                        mHideSubmeshList: list[hash] = {
                            "Stage1"
                        }
                    }
                    0xdb7fa455 = SubmeshVisibilityEventData {
                        mName: hash = 0xdb7fa455
                        mStartFrame: f32 = 33
                        mHideSubmeshList: list[hash] = {
                            "Stage2"
                        }
                    }
                    0x6d4f2733 = SubmeshVisibilityEventData {
                        mName: hash = 0x6d4f2733
                        mHideSubmeshList: list[hash] = {
                            "Cloth1"
                        }
                    }
                    0x159a6826 = SubmeshVisibilityEventData {
                        mName: hash = 0x159a6826
                        mHideSubmeshList: list[hash] = {
                            "Cloth2"
                        }
                    }
                    0x07030a82 = SubmeshVisibilityEventData {
                        mName: hash = 0x07030a82
                        mShowSubmeshList: list[hash] = {
                            "Rubble"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1.anm"
                }
            }
            0xb53c9a69 = AtomicClipData {
                mFlags: u32 = 9
                mTrackDataName: hash = "cloth"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_Turret_Chaos_Cloth_stage1.anm"
                }
            }
            0xb43c98d6 = AtomicClipData {
                mTrackDataName: hash = "cloth"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_Turret_Chaos_Cloth_stage2.anm"
                }
            }
            0x9cf732b1 = SelectorClipData {
                mFlags: u32 = 6
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = 0x2e246d03
                        mProbability: f32 = 70
                    }
                    SelectorPairData {
                        mClipName: hash = 0xfd86c944
                        mProbability: f32 = 30
                    }
                }
            }
            "Idle1_Base" = AtomicClipData {
                mFlags: u32 = 7
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1.anm"
                }
            }
            "Idle1" = ParallelClipData {
                mFlags: u32 = 7
                mClipNameList: list[hash] = {
                    0x9cf732b1
                    "Idle1_Base"
                }
            }
            "Attack2" = AtomicClipData {
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Attack1"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_idle1.anm"
                }
            }
            "Attack1" = AtomicClipData {
                mMaskDataName: hash = 0x66b411d8
                mTrackDataName: hash = "Attack1"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Turret/Skins/Skin02/Animations/SRUAP_ChaosTurret1_Idle1_seq.anm"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            0x66b411d8 = MaskData {
                mWeightList: list[f32] = {
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            "cloth" = MaskData {
                mId: u32 = 1
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
            "Attack1" = TrackData {
                mPriority: u8 = 1
            }
            "cloth" = TrackData {
                mPriority: u8 = 2
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            3324902285332737283 = TimeBlendData {
                mTime: f32 = 0
            }
            3324902285814922060 = TimeBlendData {
                mTime: f32 = 0
            }
            3324902288743656076 = TimeBlendData {
                mTime: f32 = 0
            }
            3324902288760433695 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870133176790275 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870133658975052 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870136587709068 = TimeBlendData {
                mTime: f32 = 0
            }
            5395870136604486687 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686950579531011 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686951061715788 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686953990449804 = TimeBlendData {
                mTime: f32 = 0
            }
            17974686954007227423 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746275489279235 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746275971464012 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746278900198028 = TimeBlendData {
                mTime: f32 = 0
            }
            18046746278916975647 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
