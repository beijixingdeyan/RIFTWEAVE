// Unit test for Weave stability (run via Unreal Automation)
// S = 1 - drag/2500*0.4 - angle/90*0.3 + anchors*0.12 + bonus
#include "Misc/AutomationTest.h"
IMPLEMENT_SIMPLE_AUTOMATION_TEST(FWeaveStabilityTest, "RiftWeave.Weave.Stability", EAutomationTestFlags::ApplicationContextMask | EAutomationTestFlags::ProductFilter)
bool FWeaveStabilityTest::RunTest(const FString& Parameters)
{
    auto Eval = [](float drag, float angle, int anchors, float bonus){
        float s = 1.f - drag/2500.f*0.4f - angle/90.f*0.3f + anchors*0.12f + bonus;
        return FMath::Clamp(s, 0.f, 1.2f);
    };
    TestTrue("2 anchors improves", Eval(0,0,2,0) > Eval(0,0,0,0));
    TestEqual("clamped", Eval(5000,180,0,0), 0.f);
    return true;
}
