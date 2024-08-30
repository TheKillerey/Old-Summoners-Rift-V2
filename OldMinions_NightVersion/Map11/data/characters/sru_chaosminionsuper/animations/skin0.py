#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/SRU_ChaosMinionSuper/Animations/Skin0" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Attack1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/SRU_ChaosMinionSuper/Skins/base/animations/superminion_red_attack1.anm"
                }
            }
            "Attack2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/SRU_ChaosMinionSuper/Skins/base/animations/superminion_red_attack2.anm"
                }
            }
            "Win1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/characters/sru_chaosminionsuper/skins/base/animations/superminion_red_run.anm"
                }
            }
            "Win2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/characters/sru_chaosminionsuper/skins/base/animations/superminion_red_run.anm"
                }
            }
            "Death_Base" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xee7760b0 = JointSnapEventData {
                        mStartFrame: f32 = 12
                        mEndFrame: f32 = 140
                        mJointNameToOverride: hash = 0x85c6d332
                        mJointNameToSnapTo: hash = 0xdee5d2e5
                    }
                    0x670171da = JointSnapEventData {
                        mStartFrame: f32 = 12
                        mEndFrame: f32 = 140
                        mJointNameToOverride: hash = 0xff731364
                        mJointNameToSnapTo: hash = 0x06edc917
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/SRU_ChaosMinionSuper/Skins/base/animations/superminion_red_Death.anm"
                }
            }
            0xbd31845b = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xee7760b0 = JointSnapEventData {
                        mStartFrame: f32 = 12
                        mEndFrame: f32 = 140
                        mJointNameToOverride: hash = 0x85c6d332
                        mJointNameToSnapTo: hash = 0xdee5d2e5
                    }
                    0x670171da = JointSnapEventData {
                        mStartFrame: f32 = 12
                        mEndFrame: f32 = 140
                        mJointNameToOverride: hash = 0xff731364
                        mJointNameToSnapTo: hash = 0x06edc917
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/SRU_ChaosMinionSuper/Skins/base/animations/superminion_red_death2.anm"
                }
            }
            "Idle1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/characters/sru_chaosminionsuper/skins/base/animations/superminion_red_run.anm"
                }
            }
            "Run" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/SRU_ChaosMinionSuper/Skins/base/animations/Superminion_red_run.anm"
                }
            }
            "Lose1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/characters/sru_chaosminionsuper/skins/base/animations/superminion_red_run.anm"
                }
            }
            "Lose2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/characters/sru_chaosminionsuper/skins/base/animations/superminion_red_run.anm"
                }
            }
            "Stunned" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/characters/sru_chaosminionsuper/skins/base/animations/superminion_red_run.anm"
                }
            }
            "death" = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "Death_Base"
                        mProbability: f32 = 50
                    }
                    SelectorPairData {
                        mClipName: hash = 0xbd31845b
                        mProbability: f32 = 50
                    }
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
        }
        mBlendDataTable: map[u64,pointer] = {
            3084207953292860795 = TimeBlendData {
                mTime: f32 = 0
            }
            4545597367762853243 = TimeBlendData {
                mTime: f32 = 0
            }
            4761775342492097915 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030502951525755 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208477680770427 = TimeBlendData {
                mTime: f32 = 0
            }
            7469273466910580091 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364256212655483 = TimeBlendData {
                mTime: f32 = 0
            }
            11414086196825202043 = TimeBlendData {
                mTime: f32 = 0
            }
            11486145521734950267 = TimeBlendData {
                mTime: f32 = 0
            }
            13632823077387935099 = TimeBlendData {
                mTime: f32 = 0
            }
            17110474039877737851 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
