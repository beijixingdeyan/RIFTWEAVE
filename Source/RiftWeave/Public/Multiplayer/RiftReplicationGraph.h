#pragma once
#include "CoreMinimal.h"
#include "ReplicationGraph.h"
#include "RiftReplicationGraph.generated.h"
UCLASS()
class RIFTWEAVE_API URiftReplicationGraph : public UReplicationGraph
{
    GENERATED_BODY()
public:
    virtual void InitGlobalGraphNodes() override;
    virtual void InitConnectionGraphNodes(UNetReplicationGraphConnection* Conn) override;
};
