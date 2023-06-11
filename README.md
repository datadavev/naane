# naane

NAAN Editor

- [ ] FastAPI web app
- [ ] ORCID authenticate
- [ ] NAAN entry form
- [ ] NAAN create
- [ ] NAAN list by user
- [ ] NAAN edit user auth
- [ ] Validate entry



Workflow uses GitHub API to perform CRUD operations on NAAN records.

Basically:

App deployed with NAAN records. The records have commit sha as a property. App is protected by auth.

Edit

1. Get record from GH (not from local app cache)
2. Check for existing PR. If so pull record from the PR (or deny edit until PR completed)
3. Load record into form
4. Edit
5. POST to app, app either commits or makes PR
6. GH action on commit re-generates registry


Issues:
There will be significant latency between an edit and app re-deployment. Could use a database as the content store instead of file system. Or perhaps better - use live GH as the record source when editing