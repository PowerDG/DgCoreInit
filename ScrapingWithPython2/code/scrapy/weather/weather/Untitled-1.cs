Microsoft.EntityFrameworkCore.DbUpdateException
  HResult=0x80131500
  Message=An error occurred while updating the entries. See the inner exception for details.
  Source=Microsoft.EntityFrameworkCore.Relational
  StackTrace:
   at Microsoft.EntityFrameworkCore.Update.ReaderModificationCommandBatch.Execute(IRelationalConnection connection)
   at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.Execute(DbContext _, ValueTuple`2 parameters)
   at Pomelo.EntityFrameworkCore.MySql.Storage.Internal.MySqlExecutionStrategy.Execute[TState,TResult](TState state, Func`3 operation, Func`3 verifySucceeded)
   at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.Execute(IEnumerable`1 commandBatches, IRelationalConnection connection)
   at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.SaveChanges(IReadOnlyList`1 entriesToSave)
   at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.SaveChanges(Boolean acceptAllChangesOnSuccess)
   at Microsoft.EntityFrameworkCore.DbContext.SaveChanges(Boolean acceptAllChangesOnSuccess)
   at Abp.EntityFrameworkCore.AbpDbContext.SaveChanges()
   at Abp.Zero.EntityFrameworkCore.AbpZeroCommonDbContext`3.SaveChanges()
   at DgMission.EntityFrameworkCore.Seed.Host.DefaultEditionCreator.CreateEditions() in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\Host\DefaultEditionCreator.cs:line 30
   at DgMission.EntityFrameworkCore.Seed.Host.DefaultEditionCreator.Create() in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\Host\DefaultEditionCreator.cs:line 20
   at DgMission.EntityFrameworkCore.Seed.Host.InitialHostDbBuilder.Create() in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\Host\InitialHostDbBuilder.cs:line 14
   at DgMission.EntityFrameworkCore.Seed.SeedHelper.SeedHostDb(DgMissionDbContext context) in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\SeedHelper.cs:line 25
   at DgMission.EntityFrameworkCore.Seed.SeedHelper.WithDbContext[TDbContext](IIocResolver iocResolver, Action`1 contextAction) in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\SeedHelper.cs:line 41
   at DgMission.EntityFrameworkCore.Seed.SeedHelper.SeedHostDb(IIocResolver iocResolver) in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\SeedHelper.cs:line 17
   at DgMission.EntityFrameworkCore.DgMissionEntityFrameworkModule.PostInitialize() in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\DgMissionEntityFrameworkModule.cs:line 46
   at System.Collections.Generic.List`1.ForEach(Action`1 action)
   at Abp.AbpBootstrapper.Initialize()

内部异常 1:
MySqlException: Field 'Id' doesn't have a default value

内部异常 2:
MySqlException: Field 'Id' doesn't have a default value



Microsoft.EntityFrameworkCore.DbUpdateException
  HResult=0x80131500
  Message=An error occurred while updating the entries. See the inner exception for details.
  Source=Microsoft.EntityFrameworkCore.Relational
  StackTrace:
   at Microsoft.EntityFrameworkCore.Update.ReaderModificationCommandBatch.Execute(IRelationalConnection connection)
   at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.Execute(DbContext _, ValueTuple`2 parameters)
   at Pomelo.EntityFrameworkCore.MySql.Storage.Internal.MySqlExecutionStrategy.Execute[TState,TResult](TState state, Func`3 operation, Func`3 verifySucceeded)
   at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.Execute(IEnumerable`1 commandBatches, IRelationalConnection connection)
   at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.SaveChanges(IReadOnlyList`1 entriesToSave)
   at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.SaveChanges(Boolean acceptAllChangesOnSuccess)
   at Microsoft.EntityFrameworkCore.DbContext.SaveChanges(Boolean acceptAllChangesOnSuccess)
   at Abp.EntityFrameworkCore.AbpDbContext.SaveChanges()
   at Abp.Zero.EntityFrameworkCore.AbpZeroCommonDbContext`3.SaveChanges()
   at DgMission.EntityFrameworkCore.Seed.Host.DefaultEditionCreator.CreateEditions() in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\Host\DefaultEditionCreator.cs:line 30
   at DgMission.EntityFrameworkCore.Seed.Host.DefaultEditionCreator.Create() in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\Host\DefaultEditionCreator.cs:line 20
   at DgMission.EntityFrameworkCore.Seed.Host.InitialHostDbBuilder.Create() in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\Host\InitialHostDbBuilder.cs:line 14
   at DgMission.EntityFrameworkCore.Seed.SeedHelper.SeedHostDb(DgMissionDbContext context) in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\SeedHelper.cs:line 25
   at DgMission.EntityFrameworkCore.Seed.SeedHelper.WithDbContext[TDbContext](IIocResolver iocResolver, Action`1 contextAction) in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\SeedHelper.cs:line 41
   at DgMission.EntityFrameworkCore.Seed.SeedHelper.SeedHostDb(IIocResolver iocResolver) in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\Seed\SeedHelper.cs:line 17
   at DgMission.EntityFrameworkCore.DgMissionEntityFrameworkModule.PostInitialize() in E:\GitHub\DDDgPractice\DgMission\DgMission\aspnet-core\src\DgMission.EntityFrameworkCore\EntityFrameworkCore\DgMissionEntityFrameworkModule.cs:line 46
   at System.Collections.Generic.List`1.ForEach(Action`1 action)
   at Abp.AbpBootstrapper.Initialize()

内部异常 1:
MySqlException: Field 'Id' doesn't have a default value

内部异常 2:
MySqlException: Field 'Id' doesn't have a default value
