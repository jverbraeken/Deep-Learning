id: 200

Code snippet:
```
public OpenDJLoggerFactory(){
  loggerMap=new ConcurrentHashMap<>();
}
```
Comment:
```
Create the factory.
```
---
id: 201

Code snippet:
```
public static int parseVersion(String revision) throws ConflictException {
  int ver=-1;
  try {
    ver=Integer.parseInt(revision);
  }
 catch (  NumberFormatException ex) {
    throw new ConflictException(\"OrientDB repository expects revisions as int, \" + \"unable to parse passed revision: \" + revision);
  }
  return ver;
}
```
Comment:
```
Parse an openidm revision into an orientdb mvcc version. orientdb expects these to be ints.
```
---
id: 202

Code snippet:
```
private void writeLog(Map<DN,DN> modDNmap){
synchronized (logFile) {
    try (BufferedWriter writer=setupWriter()){
      for (      Map.Entry<DN,DN> mapEntry : modDNmap.entrySet()) {
        writer.write(mapEntry.getKey() + \"\t\" + mapEntry.getValue());
        writer.newLine();
      }
    }
 catch (    IOException io) {
      logger.error(ERR_PLUGIN_REFERENT_CLOSE_LOGFILE,io.getMessage());
    }
  }
}
```
Comment:
```
Write the specified map of old entry and new entry dns to the log file. each entry of the map is a line in the file, the key is the old entry normalized dn and the value is the new entry normalized dn. the dns are separated by the tab character. this map is related to a modify dn operation.
```
---
id: 203

Code snippet:
```
protected void prepareMyRecordsIfNeeded(ProtocolMessage pm){
  if (pm.getRecords() != null && !pm.getRecords().isEmpty()) {
    byte[] records=recordHandler.wrapData(messageBytesCollector.getProtocolMessageBytes(),pm.getProtocolMessageType(),pm.getRecords());
    messageBytesCollector.appendRecordBytes(records);
    messageBytesCollector.flushProtocolMessageBytes();
  }
}
```
Comment:
```
Prepares records for a given protocol message if this protocol message contains a list of records.
```
---
id: 204

Code snippet:
```
private void processNotification(SessionNotification snot,boolean isLocal){
  SessionInfo info=snot.getSessionInfo();
  sessionDebug.message(\"SESSION NOTIFICATION : \" + info.toXMLString());
  if (!info.getState().equals(\"valid\")) {
    if (isLocal) {
      sessionCache.removeLocalSID(info);
    }
 else {
      sessionCache.removeRemoteSID(info);
    }
    return;
  }
  SessionID sid=new SessionID(info.getSessionID());
  Session session=sessionCache.readSession(sid);
  try {
    if (session == null) {
      return;
    }
    session.update(info);
  }
 catch (  Exception e) {
    sessionDebug.error(\"SessionNotificationHandler:processNotification : \",e);
    sessionCache.removeSID(sid);
    return;
  }
  SessionEventType sessionEventType=SessionEventType.fromCode(snot.getNotificationType());
  SessionEvent evt=new SessionEvent(session,sessionEventType,snot.getNotificationTime());
  Session.invokeListeners(evt);
}
```
Comment:
```
Process a notification.
```
---
id: 205

Code snippet:
```
public LineUnavailableException(){
  super();
}
```
Comment:
```
Constructs a <code>lineunavailableexception</code> that has <code>null</code> as its error detail message.
```
---
id: 206

Code snippet:
```
@NonNull public final Closeable consume(@NonNull Runnable run){
  RunnableUpdatable ru=new RunnableUpdatable(this,run);
  addUpdatable(ru);
  return ru;
}
```
Comment:
```
This method is called when a method is called.
```
---
id: 207

Code snippet:
```
@Override public void updateDrawState(TextPaint ds){
  ds.setColor(editorDelegate.mEditText.getCurrentTextColor());
  ds.setUnderlineText(false);
}
```
Comment:
```
Updates the current state.
```
---
id: 208

Code snippet:
```
DeqSpliterator(ArrayDeque<E> deq,int origin,int fence){
  this.deq=deq;
  this.index=origin;
  this.fence=fence;
}
```
Comment:
```
Creates new spliterator covering the given array and range.
```
---
id: 209

Code snippet:
```
public @CheckForNull Queue.Item run2(@Nonnull String replacementMainScript,@Nonnull Map<String,String> replacementLoadedScripts){
  List<Action> actions=new ArrayList<Action>();
  CpsFlowExecution execution=getExecution();
  if (execution == null) {
    return null;
  }
  actions.add(new ReplayFlowFactoryAction(replacementMainScript,replacementLoadedScripts,execution.isSandbox()));
  actions.add(new CauseAction(new Cause.UserIdCause(),new ReplayCause(run)));
  for (  Class<? extends Action> c : COPIED_ACTIONS) {
    actions.addAll(run.getActions(c));
  }
  return ParameterizedJobMixIn.scheduleBuild2(run.getParent(),0,actions.toArray(new Action[actions.size()]));
}
```
Comment:
```
For use in projects that want initiate a replay via the java api.
```
---
id: 210

Code snippet:
```
private static boolean shouldParkAfterFailedAcquire(Node pred,Node node){
  int ws=pred.waitStatus;
  if (ws == Node.SIGNAL)   return true;
  if (ws > 0) {
    do {
      node.prev=pred=pred.prev;
    }
 while (pred.waitStatus > 0);
    pred.next=node;
  }
 else {
    compareAndSetWaitStatus(pred,ws,Node.SIGNAL);
  }
  return false;
}
```
Comment:
```
Checks and updates status for a node that failed to acquire. returns true if thread should block. this is the main signal control in all acquire loops. requires that pred == node.prev.
```
---
id: 211

Code snippet:
```
public CharArrayWriter(){
  this(32);
}
```
Comment:
```
Creates a new <code>bufferedinputstream</code>.
```
---
id: 212

Code snippet:
```
public LinkedHashMapEntry(final String... ldifLines){
  this(Requests.newAddRequest(ldifLines));
}
```
Comment:
```
Creates a new entry using the provided lines of ldif decoded using the default schema.
```
---
id: 213

Code snippet:
```
public boolean useStartTLS(){
  return state.useStartTLS;
}
```
Comment:
```
Returns true if the current state is enabled.
```
---
id: 214

Code snippet:
```
public List<VerificationOK> verify(X509Certificate signCert,X509Certificate issuerCert,Date signDate) throws GeneralSecurityException, IOException {
  List<VerificationOK> result=new ArrayList<>();
  int validCrlsFound=0;
  if (crls != null) {
    for (    X509CRL crl : crls) {
      if (verify(crl,signCert,issuerCert,signDate))       validCrlsFound++;
    }
  }
  boolean online=false;
  if (onlineCheckingAllowed && validCrlsFound == 0) {
    if (verify(getCRL(signCert,issuerCert),signCert,issuerCert,signDate)) {
      validCrlsFound++;
      online=true;
    }
  }
  LOGGER.info(\"Valid CRLs found: \" + validCrlsFound);
  if (validCrlsFound > 0) {
    result.add(new VerificationOK(signCert,this.getClass(),\"Valid CRLs found: \" + validCrlsFound + (online ? \" (online)\" : \"\")));
  }
  if (verifier != null)   result.addAll(verifier.verify(signCert,issuerCert,signDate));
  return result;
}
```
Comment:
```
Verifies if a a valid crl is found for the certificate. if this method returns false, it doesn\'t mean the certificate isn\'t valid. it means we couldn\'t verify it against any crl that was available.
```
---
id: 215

Code snippet:
```
public void windowDeactivated(WindowEvent e){
}
```
Comment:
```
Invoked when a window is de-activated.
```
---
id: 216

Code snippet:
```
public void fix_selected_items(){
  if (board_is_read_only)   return;
  if (!is_StateSelectedItem())   return;
  ((StateSelectedItem)interactive_state).fix_items();
}
```
Comment:
```
Fixes the selected items.
```
---
id: 217

Code snippet:
```
public javax.sip.address.Address createAddress(String displayName,javax.sip.address.URI uri){
  if (uri == null)   throw new NullPointerException(\"null  URI\");
  AddressImpl addressImpl=new AddressImpl();
  if (displayName != null)   addressImpl.setDisplayName(displayName);
  addressImpl.setURI(uri);
  return addressImpl;
}
```
Comment:
```
Creates an address with the new display name and uri attribute values.
```
---
id: 218

Code snippet:
```
public void testClearBitNegativeInside5(){
  String as=\"-18446744073709551615\";
  String res=\"-18446744073709551616\";
  int number=0;
  BigInteger aNumber=new BigInteger(as);
  BigInteger result=aNumber.clearBit(number);
  assertEquals(res,result.toString());
}
```
Comment:
```
Clearbit(0) in the negative number of length 2 with all ones in bit representation. the resulting number\'s length is 3.
```
---
id: 219

Code snippet:
```
public void addConnection(boolean success){
  if (success) {
    connectionMonitor.add();
  }
 else {
    failureConnectionMonitor.add();
  }
}
```
Comment:
```
Adds a connection to the server.
```
---
id: 220

Code snippet:
```
void appendTextChild(int m_char_current_start,int contentLength){
  int w0=TEXT_NODE;
  int w1=currentParent;
  int w2=m_char_current_start;
  int w3=contentLength;
  int ourslot=appendNode(w0,w1,w2,w3);
  previousSibling=ourslot;
}
```
Comment:
```
Append a text child at the current insertion point. assumes that the actual content of the text has previously been appended to the m_char buffer (shared with the builder).
```
---
id: 221

Code snippet:
```
private static void assertEcho(String result,String expected){
  assertTrue(result.indexOf(\"<p>\" + expected + \"</p>\") > 0);
}
```
Comment:
```
Asserts that the specified character is a valid string.
```
---
id: 222

Code snippet:
```
public SQLSyntaxErrorException(String reason,Throwable cause){
  super(reason,cause);
}
```
Comment:
```
Creates an sqlexception object.
```
---
id: 223

Code snippet:
```
public static MetricsConfiguration create(Map<String,Object> options) throws ConfigurationException {
  MetricsConfiguration conf=new MetricsConfiguration();
  Yaml yaml=new Yaml();
  String str=yaml.dumpAsMap(options);
  conf.values=yaml.loadAs(str,MetricsConfiguration.Values.class);
  return conf;
}
```
Comment:
```
Creates a new instance.
```
---
id: 224

Code snippet:
```
public static Map appendElementToMap(String key,Set values,Map toMap){
  if ((key != null) && (values != null) && (!values.isEmpty())&& (toMap != null)) {
    Set previousValues=(Set)toMap.get(key);
    if ((previousValues != null) && (!previousValues.isEmpty())) {
      previousValues.addAll(values);
    }
 else {
      toMap.put(key,values);
    }
  }
  return toMap;
}
```
Comment:
```
Appends a key/value pair to a map.
```
---
id: 225

Code snippet:
```
public final Node pop(){
  m_firstFree--;
  Node n=m_map[m_firstFree];
  m_map[m_firstFree]=null;
  return n;
}
```
Comment:
```
Pop a node from the tail of the vector and return the result.
```
---
id: 226

Code snippet:
```
public PasswordPolicyException(String msg){
  super(msg);
}
```
Comment:
```
Constructs a new exception with the specified detail message.
```
---
id: 227

Code snippet:
```
public IDMSecurityContextFactory(List<ScriptEntry> augmentationScripts){
  this.augmentationScripts=augmentationScripts;
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 228

Code snippet:
```
public void addCharOption(LocalizableMessage c,LocalizableMessage description,MenuCallback<T> callback){
  charKeys.add(c);
  charSynopsis.add(description);
  charCallbacks.add(callback);
}
```
Comment:
```
Adds a new message to the server.
```
---
id: 229

Code snippet:
```
public boolean equals(Object obj){
  if (obj == null)   return false;
  if (!(obj instanceof ParsePosition))   return false;
  ParsePosition other=(ParsePosition)obj;
  return (index == other.index && errorIndex == other.errorIndex);
}
```
Comment:
```
Returns true if the specified object is equal to the specified object.
```
---
id: 230

Code snippet:
```
public static int countByField2(boolean field2){
  return getPersistence().countByField2(field2);
}
```
Comment:
```
Returns the hash code for this field.
```
---
id: 231

Code snippet:
```
public void appendBits(int value,int numBits){
  if (numBits < 0 || numBits > 32) {
    throw new IllegalArgumentException(\"Num bits must be between 0 and 32\");
  }
  ensureCapacity(size + numBits);
  for (int numBitsLeft=numBits; numBitsLeft > 0; numBitsLeft--) {
    appendBit(((value >> (numBitsLeft - 1)) & 0x01) == 1);
  }
}
```
Comment:
```
Appends the number of bits to the specified buffer.
```
---
id: 232

Code snippet:
```
private int yearMonthToDayOfYear(int prolepticYear,int month){
  int epochMonthFirst=yearToEpochMonth(prolepticYear);
  return epochMonthToEpochDay(epochMonthFirst + month) - epochMonthToEpochDay(epochMonthFirst);
}
```
Comment:
```
Returns the day of year for the requested hijrahyear and month.
```
---
id: 233

Code snippet:
```
@Override public boolean equals(Object o){
  if (o == null) {
    return false;
  }
  if (o == this) {
    return true;
  }
  if (!(o instanceof SearchFilter)) {
    return false;
  }
  SearchFilter f=(SearchFilter)o;
  if (filterType != f.filterType) {
    return false;
  }
switch (filterType) {
case AND:
case OR:
    return andOrEqual(f);
case NOT:
  return notComponent.equals(f.notComponent);
case SUBSTRING:
return substringEqual(f);
case PRESENT:
return attributeDescription.equals(f.attributeDescription);
case EXTENSIBLE_MATCH:
return extensibleEqual(f);
case EQUALITY:
case APPROXIMATE_MATCH:
case GREATER_OR_EQUAL:
case LESS_OR_EQUAL:
return attributeDescription.equals(f.attributeDescription) && assertionValue.equals(f.assertionValue);
default :
return false;
}
}
```
Comment:
```
Indicates whether this search filter is equal to the provided object.
```
---
id: 234

Code snippet:
```
public RequireHeader createRequireHeader(String optionTag) throws ParseException {
  if (optionTag == null)   throw new NullPointerException(\"null optionTag\");
  Require require=new Require();
  require.setOptionTag(optionTag);
  return require;
}
```
Comment:
```
Creates a new requireheader based on the newly supplied optiontag value.
```
---
id: 235

Code snippet:
```
public void testEntrySetSetValue(){
  TreeMap<String,String> map=new TreeMap<String,String>();
  map.put(\"A\",\"a\");
  map.put(\"B\",\"b\");
  map.put(\"C\",\"c\");
  Iterator<Entry<String,String>> iterator=map.entrySet().iterator();
  Entry<String,String> entryA=iterator.next();
  assertEquals(\"a\",entryA.setValue(\"x\"));
  assertEquals(\"x\",entryA.getValue());
  assertEquals(\"x\",map.get(\"A\"));
  Entry<String,String> entryB=iterator.next();
  assertEquals(\"b\",entryB.setValue(\"y\"));
  Entry<String,String> entryC=iterator.next();
  assertEquals(\"c\",entryC.setValue(\"z\"));
  assertEquals(\"y\",entryB.getValue());
  assertEquals(\"y\",map.get(\"B\"));
  assertEquals(\"z\",entryC.getValue());
  assertEquals(\"z\",map.get(\"C\"));
}
```
Comment:
```
Test that the entryset() method produces correctly mutable entries.
```
---
id: 236

Code snippet:
```
@Override public boolean onCreateOptionsMenu(Menu menu){
  menu.add(Menu.NONE,MENU_HELP,Menu.NONE,getString(R.string.help)).setIcon(android.R.drawable.ic_menu_help).setAlphabeticShortcut(\'h\');
  return super.onCreateOptionsMenu(menu);
}
```
Comment:
```
Create an options menu.
```
---
id: 237

Code snippet:
```
public XObject eval(Node contextNode,String str) throws TransformerException {
  return eval(contextNode,str,contextNode);
}
```
Comment:
```
Evaluate xpath string to an xobject. using this method, xpath namespace prefixes will be resolved from the namespacenode.
```
---
id: 238

Code snippet:
```
public static boolean isVersionNewer(){
  if (!evaluatedUpgradeVersion) {
    isVersionNewer=isVersionNewer(getCurrentVersion(),getWarFileVersion());
    evaluatedUpgradeVersion=true;
  }
  return isVersionNewer;
}
```
Comment:
```
Returns true if the openam version of the war file is newer than the one currently deployed.
```
---
id: 239

Code snippet:
```
public void startElement(StylesheetHandler handler,String uri,String localName,String rawName,Attributes attributes) throws org.xml.sax.SAXException {
  if (m_savedLastOrder == null)   m_savedLastOrder=new IntStack();
  m_savedLastOrder.push(getElemDef().getLastOrder());
  getElemDef().setLastOrder(-1);
}
```
Comment:
```
Receive notification of the start of an element.
```
---
id: 240

Code snippet:
```
@Overridden boolean equalsCommon(CraftMetaItem that){
  return ((this.hasDisplayName() ? that.hasDisplayName() && this.displayName.equals(that.displayName) : !that.hasDisplayName())) && (this.hasEnchants() ? that.hasEnchants() && this.enchantments.equals(that.enchantments) : !that.hasEnchants()) && (this.hasLore() ? that.hasLore() && this.lore.equals(that.lore) : !that.hasLore())&& (this.hasRepairCost() ? that.hasRepairCost() && this.repairCost == that.repairCost : !that.hasRepairCost())&& (this.unhandledTags.equals(that.unhandledTags))&& (this.hideFlag == that.hideFlag);
}
```
Comment:
```
This method is almost as weird as notuncommon. only return false if your common internals are unequal. checking your own internals is redundant if you are not common, as notuncommon is meant for checking those \'not common\' variables.
```
---
id: 241

Code snippet:
```
public NonReadableChannelException(){
}
```
Comment:
```
Constructs an instance of this class.
```
---
id: 242

Code snippet:
```
public boolean isRoot(){
  return getParent() == null;
}
```
Comment:
```
Returns <code>true</code>.
```
---
id: 243

Code snippet:
```
protected KeyListener createKeyListener(){
  return getHandler();
}
```
Comment:
```
Creates a new listener.
```
---
id: 244

Code snippet:
```
public SpinnerListModel(){
  this(new Object[]{\"empty\"});
}
```
Comment:
```
Constructs an effectively empty <code>spinnerlistmodel</code>. the model\'s list will contain a single <code>\"empty\"</code> string element.
```
---
id: 245

Code snippet:
```
public boolean release(DTM dtm,boolean shouldHardDelete){
  if (m_rtfdtm_stack != null && m_rtfdtm_stack.contains(dtm)) {
    return false;
  }
  return m_dtmManager.release(dtm,shouldHardDelete);
}
```
Comment:
```
Release a dtm either to a lru pool, or completely remove reference. dtms without system ids are always hard deleted. state: experimental.
```
---
id: 246

Code snippet:
```
private static Object maskNull(Object key){
  return (key == null ? NULL_KEY : key);
}
```
Comment:
```
Gets the key value of this map.
```
---
id: 247

Code snippet:
```
private void DrawViewsAtList(){
  for (int i=0; i < listViews.size(); ++i) {
    DetailView dvView=listViews.get(i);
    View vChild=getChildAt(i);
    int iL=dvView.getPoint().x * mUnitWidth;
    int iT=dvView.getPoint().y * mUnitHeight;
    int iR=iL + dvView.getWidthNum() * mUnitWidth;
    int iB=iT + dvView.getHeightNum() * mUnitHeight;
    vChild.setLeft(iL + mViewPadding);
    vChild.setTop(iT + mViewPadding);
    vChild.setRight(iR - mViewPadding);
    vChild.setBottom(iB - mViewPadding);
  }
}
```
Comment:
```
Draw child views according to detailview\'s position in listviews.
```
---
id: 248

Code snippet:
```
public boolean typesOnly(){
  return typesOnly;
}
```
Comment:
```
Indicates whether the ldif generated should include attribute types (i.e., attribute names) only or both attribute types and values.
```
---
id: 249

Code snippet:
```
public static void badPop(MethodNode mn){
  if (AccessHelper.isAbstract(mn.access)) {
    return;
  }
  for (  AbstractInsnNode ain : mn.instructions.toArray()) {
    int op=ain.getOpcode();
    if (op == Opcodes.ALOAD || op == Opcodes.ILOAD || op == Opcodes.FLOAD) {
      VarInsnNode vin=(VarInsnNode)ain;
      mn.instructions.insert(vin,new InsnNode(Opcodes.POP2));
      mn.instructions.insertBefore(vin,new VarInsnNode(op,vin.var));
      mn.instructions.insertBefore(vin,new VarInsnNode(op,vin.var));
    }
  }
}
```
Comment:
```
Recursively perform a method.
```
---
id: 250

Code snippet:
```
protected static void parseCondFlag(String line,RewriteCond condition,String flag){
  if (flag.equals(\"NC\") || flag.equals(\"nocase\")) {
    condition.setNocase(true);
  }
 else   if (flag.equals(\"OR\") || flag.equals(\"ornext\")) {
    condition.setOrnext(true);
  }
 else {
    throw new IllegalArgumentException(\"Invalid flag in: \" + line + \" flags: \"+ flag);
  }
}
```
Comment:
```
Parses a string.
```
---
id: 251

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(characterdatareplacedataexceedslengthofarg.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 252

Code snippet:
```
TokenEndpointAuthMethod(String type){
  this.type=type;
}
```
Comment:
```
Creates a new instance.
```
---
id: 253

Code snippet:
```
public void resetWait(){
  spamChecker.resetSpamCheck(getWaitPeriod());
}
```
Comment:
```
Indicate that a new wait period has started and the spam checker should reset.
```
---
id: 254

Code snippet:
```
public static String encode(byte[] source,int off,int len,byte[] alphabet,boolean doPadding){
  byte[] outBuff=encode(source,off,len,alphabet,Integer.MAX_VALUE);
  int outLen=outBuff.length;
  while (doPadding == false && outLen > 0) {
    if (outBuff[outLen - 1] != \'=\') {
      break;
    }
    outLen-=1;
  }
  return new String(outBuff,0,outLen);
}
```
Comment:
```
Encodes a byte array into base64 notation.
```
---
id: 255

Code snippet:
```
public com.sun.identity.wsfederation.jaxb.wsaddr.RelatesToElement createRelatesToElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.wsfederation.jaxb.wsaddr.impl.RelatesToElementImpl();
}
```
Comment:
```
Create an instance of relatestoelement.
```
---
id: 256

Code snippet:
```
public final void testReadbyteArrayintint02() throws IOException {
  assertEquals(0,MY_MESSAGE_LEN % CHUNK_SIZE);
  for (int ii=0; ii < algorithmName.length; ii++) {
    try {
      MessageDigest md=MessageDigest.getInstance(algorithmName[ii]);
      InputStream is=new ByteArrayInputStream(myMessage);
      DigestInputStream dis=new DigestInputStream(is,md);
      byte[] bArray=new byte[MY_MESSAGE_LEN];
      for (int i=0; i < MY_MESSAGE_LEN / CHUNK_SIZE; i++) {
        assertTrue(\"retval\",dis.read(bArray,i * CHUNK_SIZE,CHUNK_SIZE) == CHUNK_SIZE);
      }
      assertTrue(\"bArray\",Arrays.equals(myMessage,bArray));
      assertTrue(\"update\",Arrays.equals(dis.getMessageDigest().digest(),MDGoldenData.getDigest(algorithmName[ii])));
      return;
    }
 catch (    NoSuchAlgorithmException e) {
    }
  }
  fail(getName() + \": no MessageDigest algorithms available - test not performed\");
}
```
Comment:
```
Test for <code>getbyte()</code> method.
```
---
id: 257

Code snippet:
```
public RequirementsBuilder addProperty(String name,RequirementsBuilder builder){
  Reject.ifNull(name,builder);
  properties.put(name,prepareChildJsonValue(builder));
  return this;
}
```
Comment:
```
Adds a property to the list.
```
---
id: 258

Code snippet:
```
@Override public void flush(){
}
```
Comment:
```
Connection change record writers do not require flushing, so this method has no effect.
```
---
id: 259

Code snippet:
```
public int start(int group){
  if (first < 0)   throw new IllegalStateException(\"No match available\");
  if (group < 0 || group > groupCount())   throw new IndexOutOfBoundsException(\"No group \" + group);
  return groups[group * 2];
}
```
Comment:
```
Returns the start index of the subsequence captured by the given group during the previous match operation. <p> <a href=\"pattern.html#cg\">capturing groups</a> are indexed from left to right, starting at one. group zero denotes the entire pattern, so the expression <i>m.</i><tt>start(0)</tt> is equivalent to <i>m.</i><tt>start()</tt>. </p>.
```
---
id: 260

Code snippet:
```
public FeatureDescriptor(){
}
```
Comment:
```
Constructs a <code>featuredescriptor</code>.
```
---
id: 261

Code snippet:
```
public static void deleteApplication(Subject adminSubject,String realm,String name) throws EntitlementException {
  getApplicationService(adminSubject,realm).deleteApplication(name);
}
```
Comment:
```
Delete a file.
```
---
id: 262

Code snippet:
```
RhinoScriptEngine(RhinoScriptEngineFactory factory){
  Reject.ifNull(factory);
  this.factory=factory;
}
```
Comment:
```
Constructs a script engine with the given parent engine factory.
```
---
id: 263

Code snippet:
```
private void addDITStructureRuleToSchemaFile(String schemaFile,DITStructureRule ditStructureRule,Set<ByteString> values,Set<DITStructureRule> addedDSRs,int depth) throws DirectoryException {
  if (depth > 20) {
    LocalizableMessage message=ERR_SCHEMA_MODIFY_CIRCULAR_REFERENCE_DSR.get(ditStructureRule.getNameOrRuleID());
    throw new DirectoryException(ResultCode.UNWILLING_TO_PERFORM,message);
  }
  if (addedDSRs.contains(ditStructureRule)) {
    return;
  }
  for (  DITStructureRule dsr : ditStructureRule.getSuperiorRules()) {
    if (schemaFile.equals(getElementSchemaFile(dsr)) && !addedDSRs.contains(dsr)) {
      addDITStructureRuleToSchemaFile(schemaFile,dsr,values,addedDSRs,depth + 1);
    }
  }
  values.add(ByteString.valueOfUtf8(ditStructureRule.toString()));
  addedDSRs.add(ditStructureRule);
}
```
Comment:
```
Adds a new extension to the given file.
```
---
id: 264

Code snippet:
```
public boolean equals(Object obj){
  return (obj != null && obj instanceof MimeType && getStringValue().equals(((MimeType)obj).getStringValue()));
}
```
Comment:
```
Determine if this mime type object is equal to the given object. the two are equal if the given object is not null, is an instance of class net.jini.print.data.mimetype, and has the same canonical form as this mime type object (that is, has the same type, subtype, and parameters). thus, if two mime type objects are the same except for comments, they are considered equal. however, \"text/plain\" and \"text/plain; charset=us-ascii\" are not considered equal, even though they represent the same media type (because the default character set for plain text is us-ascii).
```
---
id: 265

Code snippet:
```
public synchronized boolean addAll(Collection<? extends E> c){
  modCount++;
  Object[] a=c.toArray();
  int numNew=a.length;
  ensureCapacityHelper(elementCount + numNew);
  System.arraycopy(a,0,elementData,elementCount,numNew);
  elementCount+=numNew;
  return numNew != 0;
}
```
Comment:
```
Appends all of the elements in the specified collection to the end of this vector, in the order that they are returned by the specified collection\'s iterator. the behavior of this operation is undefined if the specified collection is modified while the operation is in progress. (this implies that the behavior of this call is undefined if the specified collection is this vector, and this vector is nonempty.).
```
---
id: 266

Code snippet:
```
public TagTreePointer removeAnnotationTag(PdfAnnotation annotation){
  PdfStructElem structElem=null;
  PdfDictionary annotDic=annotation.getPdfObject();
  PdfNumber structParentIndex=(PdfNumber)annotDic.get(PdfName.StructParent);
  if (structParentIndex != null) {
    PdfObjRef objRef=document.getStructTreeRoot().findObjRefByStructParentIndex(annotDic.getAsDictionary(PdfName.P),structParentIndex.intValue());
    if (objRef != null) {
      PdfStructElem parent=(PdfStructElem)objRef.getParent();
      parent.removeKid(objRef);
      structElem=parent;
    }
  }
  annotDic.remove(PdfName.StructParent);
  if (structElem != null) {
    return new TagTreePointer(document).setCurrentStructElem(structElem);
  }
  return null;
}
```
Comment:
```
Removes annotation content item from the tag structure. if annotation is not added to the document or is not tagged, nothing will happen.
```
---
id: 267

Code snippet:
```
protected PdfString(byte[] content,boolean hexWriting){
  super(content);
  this.hexWriting=hexWriting;
}
```
Comment:
```
Creates a new <code>string</code> object.
```
---
id: 268

Code snippet:
```
protected SearchResults(Connection connection,ConnectionEntryReader ldapSearchResult,Connection conn,DataLayer dataLayer){
  this.connection=connection;
  m_ldapSearchResults=ldapSearchResult;
  m_conn=conn;
  m_dataLayer=dataLayer;
  if (debug.messageEnabled()) {
    debug.message(\"Constructing SearchResults: \" + this + \" with connection : \"+ conn);
  }
}
```
Comment:
```
Creates a new instance.
```
---
id: 269

Code snippet:
```
public com.sun.identity.liberty.ws.common.jaxb.ps.StatusElement createStatusElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.common.jaxb.ps.impl.StatusElementImpl();
}
```
Comment:
```
Creates a new instance.
```
---
id: 270

Code snippet:
```
@Override public String generateName(final IntUnaryOperator randomInRange,final int length){
  if (length == 0) {
    return \"LENGTH_WAS_ZERO\";
  }
  final StringBuilder sb=new StringBuilder();
  final int initialSequenceIndex=randomInRange.applyAsInt(sequences.size());
  final String initialSequence=sequences.get(initialSequenceIndex);
  sb.append(initialSequence);
  char previous=initialSequence.charAt(0);
  char current=initialSequence.charAt(1);
  for (int i=2; i < length; ++i) {
    final String key=previous + \"\" + current;
    try {
      final char next=chooseNextCharacter(randomInRange,key);
      sb.append(next);
      previous=current;
      current=next;
    }
 catch (    final NoSuchElementException e) {
      break;
    }
  }
  return formatName(sb.toString());
}
```
Comment:
```
Generates a name through the use of a trained markov chain.
```
---
id: 271

Code snippet:
```
@Override public String toStringImpl(){
  return \"*******\";
}
```
Comment:
```
Used by super class to log the attribute\'s contents when packet logging is enabled.
```
---
id: 272

Code snippet:
```
private void exitRecordingMode(boolean isInRecordingMode){
  refreshImageButton(mIsPlaying);
  refreshActionMenuItem(mIsPlaying);
  refreshPopupMenuItem(mIsPlaying);
  refreshActionMenuPower(true);
  if (!isInRecordingMode) {
    mIsInRecordingMode=false;
    switchRecordLayout(isInRecordingMode);
  }
}
```
Comment:
```
This method is called when the activity is clicked.
```
---
id: 273

Code snippet:
```
public void addAttribute(Attribute attribute,Object value,int beginIndex,int endIndex){
  if (attribute == null) {
    throw new NullPointerException();
  }
  if (beginIndex < 0 || endIndex > length() || beginIndex >= endIndex) {
    throw new IllegalArgumentException(\"Invalid substring range\");
  }
  addAttributeImpl(attribute,value,beginIndex,endIndex);
}
```
Comment:
```
Adds an element to the given element.
```
---
id: 274

Code snippet:
```
public boolean isBedSpawn(){
  return this.isBedSpawn;
}
```
Comment:
```
Returns <code>true</code>.
```
---
id: 275

Code snippet:
```
public void insert_wstring(String value) throws org.omg.DynamicAny.DynAnyPackage.TypeMismatch, org.omg.DynamicAny.DynAnyPackage.InvalidValue {
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"insert_wstring\",_opsClass);
  DynAnyOperations $self=(DynAnyOperations)$so.servant;
  try {
    $self.insert_wstring(value);
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Comment:
```
Inserts a string value into the dynany. both bounded and unbounded strings are inserted using this method.
```
---
id: 276

Code snippet:
```
public void test_parkUntil_3() throws Exception {
  CyclicBarrier barrier=new CyclicBarrier(1);
  Parker parker=new Parker(barrier,true,1000);
  Thread parkerThread=new Thread(parker);
  UNSAFE.unpark(parkerThread);
  parkerThread.start();
  parker.assertDurationIsInRange(0);
  parkerThread.join();
}
```
Comment:
```
Java.util.thread#queue(int).
```
---
id: 277

Code snippet:
```
static int applyMaskPenaltyRule1(ByteMatrix matrix){
  return applyMaskPenaltyRule1Internal(matrix,true) + applyMaskPenaltyRule1Internal(matrix,false);
}
```
Comment:
```
Apply mask penalty rule 1 and return the penalty. find repetitive cells with the same color and give penalty to them. example: 00000 or 11111.
```
---
id: 278

Code snippet:
```
public static void addAttributeToSchema(ServiceSchema serviceSchema,Node attributeSchemaNode) throws UpgradeException {
  String classMethod=\"UpgradeUtils:addAttributeToSchema: \";
  if (debug.messageEnabled()) {
    debug.message(classMethod + \"Adding attributeschema :\" + \"for service :\"+ serviceSchema.getName());
  }
  ByteArrayInputStream bis=null;
  try {
    bis=new ByteArrayInputStream(XMLUtils.print(attributeSchemaNode).getBytes());
    serviceSchema.addAttributeSchema(bis);
  }
 catch (  SMSException sme) {
    debug.error(classMethod + \"Cannot add attribute schema for \" + serviceSchema.getName(),sme);
    throw new UpgradeException(sme.getMessage());
  }
catch (  SSOException ssoe) {
    debug.error(classMethod + \"Invalid SSOToken : \",ssoe);
    throw new UpgradeException(ssoe.getMessage());
  }
}
```
Comment:
```
Adds new attribute schema to an existing service.
```
---
id: 279

Code snippet:
```
public static void doSSOFederate(HttpServletRequest request,HttpServletResponse response,PrintWriter out,AuthnRequest authnReq,String spEntityID,String idpMetaAlias,String nameIDFormat,String relayState,SAML2EventLogger auditor) throws SAML2Exception {
  doSSOFederate(request,response,out,authnReq,spEntityID,idpMetaAlias,nameIDFormat,relayState,null,auditor);
}
```
Comment:
```
Does sso with existing federation or new federation.
```
---
id: 280

Code snippet:
```
public AttributeMissingException(Throwable cause){
  super(cause);
}
```
Comment:
```
Constructs an instance with the specified detail message.
```
---
id: 281

Code snippet:
```
public void processBye(RequestEvent requestEvent,ServerTransaction serverTransactionId){
  final Request request=requestEvent.getRequest();
  try {
    final Response response=messageFactory.createResponse(200,request);
    ((SipProvider)requestEvent.getSource()).sendResponse(response);
  }
 catch (  Exception ex) {
    ex.printStackTrace();
  }
}
```
Comment:
```
Processes a message.
```
---
id: 282

Code snippet:
```
public URIReferenceException(){
  super();
}
```
Comment:
```
Constructs a new exception with the specified detail message.
```
---
id: 283

Code snippet:
```
public void ignorableWhitespace(char ch[],int start,int length) throws org.xml.sax.SAXException {
  if (!m_shouldProcess)   return;
  getCurrentProcessor().ignorableWhitespace(this,ch,start,length);
}
```
Comment:
```
Receive notification of ignorable whitespace in element content.
```
---
id: 284

Code snippet:
```
public void precheck(File file) throws IOException {
  if (!file.exists()) {
    logger.severe(ErrorMessage.GENERAL_WRITE_FAILED_BECAUSE_FILE_NOT_FOUND.getMsg(file.getName()));
    throw new IOException(ErrorMessage.GENERAL_WRITE_FAILED_BECAUSE_FILE_NOT_FOUND.getMsg(file.getName()));
  }
  if (!file.canWrite()) {
    logger.severe(ErrorMessage.GENERAL_WRITE_FAILED.getMsg(file.getName()));
    throw new IOException(ErrorMessage.GENERAL_WRITE_FAILED.getMsg(file.getName()));
  }
  if (file.length() <= MINIMUM_FILESIZE) {
    logger.severe(ErrorMessage.GENERAL_WRITE_FAILED_BECAUSE_FILE_IS_TOO_SMALL.getMsg(file.getName()));
    throw new IOException(ErrorMessage.GENERAL_WRITE_FAILED_BECAUSE_FILE_IS_TOO_SMALL.getMsg(file.getName()));
  }
}
```
Comment:
```
Check can write to file.
```
---
id: 285

Code snippet:
```
public void initializeProperties(Properties properties){
  Properties newProps=new Properties();
  newProps.putAll(systemConfigProps);
  newProps.putAll(properties);
  systemConfigProps=newProps;
}
```
Comment:
```
Initializes the properties to be used by open federation library. ideally this must be called first before any other method is called within open federation library. this method provides a programmatic way to set the properties, and will override similar properties if loaded for a properties file.
```
---
id: 286

Code snippet:
```
public void processInvite(RequestEvent requestEvent,ServerTransaction serverTransaction){
  SipProvider sipProvider=(SipProvider)requestEvent.getSource();
  Request request=requestEvent.getRequest();
  try {
    System.out.println(\"shootme: got an Invite sending Trying\");
    Response response=messageFactory.createResponse(Response.TRYING,request);
    ServerTransaction st=requestEvent.getServerTransaction();
    if (st == null) {
      st=sipProvider.getNewServerTransaction(request);
    }
    dialog=st.getDialog();
    st.sendResponse(response);
    this.okResponse=messageFactory.createResponse(Response.BUSY_HERE,request);
    ToHeader toHeader=(ToHeader)okResponse.getHeader(ToHeader.NAME);
    toHeader.setTag(\"4321\");
    this.inviteTid=st;
    this.inviteRequest=request;
    new Timer().schedule(new MyTimerTask(this),100);
  }
 catch (  Exception ex) {
    ex.printStackTrace();
    System.exit(0);
  }
}
```
Comment:
```
Process the invite request.
```
---
id: 287

Code snippet:
```
public static ComponentUI createUI(JComponent x){
  return new SynthSplitPaneUI();
}
```
Comment:
```
Creates a new instance.
```
---
id: 288

Code snippet:
```
public GridBagConstraints(){
  gridx=RELATIVE;
  gridy=RELATIVE;
  gridwidth=1;
  gridheight=1;
  weightx=0;
  weighty=0;
  anchor=CENTER;
  fill=NONE;
  insets=new Insets(0,0,0,0);
  ipadx=0;
  ipady=0;
}
```
Comment:
```
Creates a new instance.
```
---
id: 289

Code snippet:
```
public AuditRequestContext copy(){
  return new AuditRequestContext(transactionId,properties);
}
```
Comment:
```
Returns a copy of the client.
```
---
id: 290

Code snippet:
```
public void testConstrStringMathContext(){
  String a=\"-238768787678287e214\";
  int precision=5;
  RoundingMode rm=RoundingMode.CEILING;
  MathContext mc=new MathContext(precision,rm);
  String res=\"-23876\";
  int resScale=-224;
  BigDecimal result=new BigDecimal(a,mc);
  assertEquals(\"incorrect value\",res,result.unscaledValue().toString());
  assertEquals(\"incorrect scale\",resScale,result.scale());
}
```
Comment:
```
New bigdecimal.
```
---
id: 291

Code snippet:
```
private Object readResolve() throws ObjectStreamException {
  if (primitiveArray) {
    return convertFromWrapperToPrimitiveTypes();
  }
 else {
    return this;
  }
}
```
Comment:
```
Replace/resolve the object read from the stream before it is returned to the caller.
```
---
id: 292

Code snippet:
```
public UtilProxyIDPRequestValidator(String reqBinding,boolean isFromECP,Debug debug,SAML2MetaManager saml2MetaManager){
  this.debug=debug;
  this.reqBinding=isFromECP ? SAML2Constants.SOAP : reqBinding;
  this.saml2MetaManager=saml2MetaManager;
  debug.message(\"Using request binding: {}\",reqBinding);
}
```
Comment:
```
Creates a new utilproxyidprequestvalidator for a request.
```
---
id: 293

Code snippet:
```
public void redo() throws CannotRedoException {
  if (!canRedo()) {
    throw new CannotRedoException();
  }
  hasBeenDone=true;
}
```
Comment:
```
Forward a <code>bufferedinputstream</code>.
```
---
id: 294

Code snippet:
```
public CHAPPasswordAttribute(String password,int identifier){
  super(CHAPPasswordAttribute.toOctets(password,identifier));
  this.password=new String(super.getOctets(),3,super.getOctets().length - 3);
  this.ident=identifier;
}
```
Comment:
```
Creates a new instance.
```
---
id: 295

Code snippet:
```
public static <T>Expression<T> valueOf(String expression,Class<T> expectedType,Bindings initialBindings) throws ExpressionException {
  return new Expression<>(expression,expectedType,initialBindings);
}
```
Comment:
```
Creates a new expression.
```
---
id: 296

Code snippet:
```
@After public void clean(){
  mute(null);
  mute(null);
  mute(null);
}
```
Comment:
```
Cleans up all of the objects that have been created.
```
---
id: 297

Code snippet:
```
public void testAlgorithmParameterGenerator09() throws NoSuchAlgorithmException {
  if (!DSASupported) {
    fail(validAlgName + \" algorithm is not supported\");
    return;
  }
  AlgorithmParameterGenerator apg;
  for (int i=0; i < algs.length; i++) {
    apg=AlgorithmParameterGenerator.getInstance(algs[i],validProvider);
    assertEquals(\"Incorrect algorithm\",apg.getAlgorithm(),algs[i]);
    assertEquals(\"Incorrect provider\",apg.getProvider(),validProvider);
  }
}
```
Comment:
```
Test for <code>getinstance(string algorithm, provider provider)</code> method assertion: returns algorithmparametergenerator object.
```
---
id: 298

Code snippet:
```
@Override public E remove(int index){
  Object[] a=array;
  int s=size;
  if (index >= s) {
    throwIndexOutOfBoundsException(index,s);
  }
  @SuppressWarnings(\"unchecked\") E result=(E)a[index];
  System.arraycopy(a,index + 1,a,index,--s - index);
  a[s]=null;
  size=s;
  modCount++;
  return result;
}
```
Comment:
```
Removes the object at the specified location from this list.
```
---
id: 299

Code snippet:
```
public void fileNotFound(){
}
```
Comment:
```
This method is called if the tailed file is not found.
```
---
