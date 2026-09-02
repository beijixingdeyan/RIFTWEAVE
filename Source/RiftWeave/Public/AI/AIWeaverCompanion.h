#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "AIWeaverCompanion.generated.h"
class UStateTreeComponent;
/// AI companion for single-player — fills anchor role via StateTree + SmartObject.
UCLASS()
class RIFTWEAVE_API AAIWeaverCompanion : public ACharacter
{
    GENERATED_BODY()
public:
    AAIWeaverCompanion();
    UPROPERTY(VisibleAnywhere, Category="AI") TObjectPtr<UStateTreeComponent> StateTreeComp;
    UFUNCTION(BlueprintCallable) void CommandAnchor(FVector Location);
    UFUNCTION(BlueprintCallable) void FollowPlayer(AActor* Player);
protected:
    virtual void BeginPlay() override;
};
