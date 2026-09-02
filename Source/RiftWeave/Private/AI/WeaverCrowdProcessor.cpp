#include "AI/WeaverCrowdProcessor.h"
#include "AI/MassWeaverAI.h"
UWeaverCrowdProcessor::UWeaverCrowdProcessor(){ ExecutionFlags = (int32)EProcessorExecutionFlags::All; }
void UWeaverCrowdProcessor::ConfigureQueries(const TSharedRef<FMassEntityManager>& EM){ HerdQuery.AddRequirement<FFragment_FrostElk>(EMassFragmentAccess::ReadWrite); HerdQuery.AddTagRequirement<FTag_InRift>(EMassFragmentPresence::None); }
void UWeaverCrowdProcessor::Execute(FMassEntityManager& EM, FMassExecutionContext& Ctx){ HerdQuery.ForEachEntityChunk(EM,Ctx,[](FMassExecutionContext& C){ auto& Elks=C.GetMutableFragment<FFragment_FrostElk>(); }); }
