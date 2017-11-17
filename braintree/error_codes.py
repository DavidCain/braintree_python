class ErrorCodes(object):
    """
    A set of constants representing validation errors.  Validation error messages can change, but the codes will not.
    See the source for a list of all errors codes.

    Codes can be used to check for specific validation errors::

        result = Transaction.sale({})
        assert(result.is_success == False)
        assert(result.errors.for_object("transaction").on("amount")[0].code == ErrorCodes.Transaction.AmountIsRequired)
    """

    class Address(object):
        CannotBeBlank = "81801"
        CompanyIsInvalid = "91821"
        CompanyIsTooLong = "81802"
        CountryCodeAlpha2IsNotAccepted = "91814"
        CountryCodeAlpha3IsNotAccepted = "91816"
        CountryCodeNumericIsNotAccepted = "91817"
        CountryNameIsNotAccepted = "91803"
        ExtedAddressIsTooLong = "81804" # Deprecated
        ExtendedAddressIsInvalid = "91823"
        ExtendedAddressIsTooLong = "81804"
        FirstNameIsInvalid = "91819"
        FirstNameIsTooLong = "81805"
        InconsistentCountry = "91815"
        IsInvalid = "91828"
        LastNameIsInvalid = "91820"
        LastNameIsTooLong = "81806"
        LocalityIsInvalid = "91824"
        LocalityIsTooLong = "81807"
        PostalCodeInvalidCharacters = "81813"
        PostalCodeIsInvalid = "91826"
        PostalCodeIsRequired = "81808"
        PostalCodeIsTooLong = "81809"
        RegionIsInvalid = "91825"
        RegionIsTooLong = "81810"
        StateIsInvalidForSellerProtection = "81827"
        StreetAddressIsInvalid = "91822"
        StreetAddressIsRequired = "81811"
        StreetAddressIsTooLong = "81812"
        TooManyAddressesPerCustomer = "91818"

    class ApplePay(object):
        ApplePayCardsAreNotAccepted = "83501"
        CustomerIdIsRequiredForVaulting = "83502"
        TokenIsInUse = "93503"
        PaymentMethodNonceConsumed = "93504"
        PaymentMethodNonceUnknown = "93505"
        PaymentMethodNonceLocked = "93506"
        PaymentMethodNonceCardTypeIsNotAccepted = "83518"
        CannotUpdateApplePayCardUsingPaymentMethodNonce = "93507"
        NumberIsRequired = "93508"
        ExpirationMonthIsRequired = "93509"
        ExpirationYearIsRequired = "93510"
        CryptogramIsRequired = "93511"
        DecryptionFailed = "83512"
        Disabled = "93513"
        MerchantNotConfigured = "93514"
        MerchantKeysAlreadyConfigured = "93515"
        MerchantKeysNotConfigured = "93516"
        CertificateInvalid = "93517"
        CertificateMismatch = "93519"
        InvalidToken = "83520"
        PrivateKeyMismatch = "93521"
        KeyMismatchStoringCertificate = "93522"

    class AuthorizationFingerprint(object):
        MissingFingerprint = "93201"
        InvalidFormat = "93202"
        SignatureRevoked = "93203"
        InvalidCreatedAt = "93204"
        InvalidPublicKey = "93205"
        InvalidSignature = "93206"
        OptionsNotAllowedWithoutCustomer = "93207"

    class ClientToken(object):
        MakeDefaultRequiresCustomerId = "92801"
        VerifyCardRequiresCustomerId = "92802"
        FailOnDuplicatePaymentMethodRequiresCustomerId = "92803"
        CustomerDoesNotExist = "92804"
        ProxyMerchantDoesNotExist = "92805"
        UnsupportedVersion = "92806"
        MerchantAccountDoesNotExist = "92807"

    class CreditCard(object):
        BillingAddressConflict = "91701"
        BillingAddressFormatIsInvalid = "91744"
        BillingAddressIdIsInvalid = "91702"
        CannotUpdateCardUsingPaymentMethodNonce = "91735"
        CannotUpdateCardUsingPaymentMethodNonce = "91735"
        CardholderNameIsTooLong = "81723"
        CreditCardTypeIsNotAccepted = "81703"
        CreditCardTypeIsNotAcceptedBySubscriptionMerchantAccount = "81718"
        CustomerIdIsInvalid = "91705"
        CustomerIdIsRequired = "91704"
        CvvIsInvalid = "81707"
        CvvIsRequired = "81706"
        CvvVerificationFailed = "81736"
        DuplicateCardExists = "81724"
        ExpirationDateConflict = "91708"
        ExpirationDateIsInvalid = "81710"
        ExpirationDateIsRequired = "81709"
        ExpirationDateYearIsInvalid = "81711"
        ExpirationMonthIsInvalid = "81712"
        ExpirationYearIsInvalid = "81713"
        InvalidParamsForCreditCardUpdate = "91745"
        InvalidVenmoSDKPaymentMethodCode = "91727"
        NumberHasInvalidLength = NumberLengthIsInvalid = "81716"
        NumberIsInvalid = "81715"
        NumberIsProhibited = "81750"
        NumberIsRequired = "81714"
        NumberMustBeTestNumber = "81717"
        PaymentMethodConflict = "81725"
        PaymentMethodIsNotACreditCard = "91738"
        PaymentMethodNonceCardTypeIsNotAccepted = "91734"
        PaymentMethodNonceCardTypeIsNotAccepted = "91734"
        PaymentMethodNonceConsumed = "91731"
        PaymentMethodNonceConsumed = "91731"
        PaymentMethodNonceLocked = "91733"
        PaymentMethodNonceLocked = "91733"
        PaymentMethodNonceUnknown = "91732"
        PaymentMethodNonceUnknown = "91732"
        PostalCodeVerificationFailed = "81737"
        TokenInvalid = TokenFormatIsInvalid = "91718"
        TokenIsInUse = "91719"
        TokenIsNotAllowed = "91721"
        TokenIsRequired = "91722"
        TokenIsTooLong = "91720"
        VenmoSDKPaymentMethodCodeCardTypeIsNotAccepted = "91726"
        VerificationNotSupportedOnThisMerchantAccount = "91730"

        class Options(object):
            UpdateExistingTokenIsInvalid = "91723"
            UpdateExistingTokenNotAllowed = "91729"
            VerificationAmountCannotBeNegative = "91739"
            VerificationAmountFormatIsInvalid = "91740"
            VerificationAmountIsTooLarge = "91752"
            VerificationAmountNotSupportedByProcessor = "91741"
            VerificationMerchantAccountIdIsInvalid = "91728"
            VerificationMerchantAccountIsForbidden = "91743"
            VerificationMerchantAccountIsSuspended = "91742"
            VerificationMerchantAccountCannotBeSubMerchantAccount = "91755"


    class Customer(object):
        CompanyIsTooLong = "81601"
        CustomFieldIsInvalid = "91602"
        CustomFieldIsTooLong = "81603"
        EmailIsInvalid = EmailFormatIsInvalid = "81604"
        EmailIsRequired = "81606"
        EmailIsTooLong = "81605"
        FaxIsTooLong = "81607"
        FirstNameIsTooLong = "81608"
        IdIsInUse = "91609"
        IdIsInvaild = "91610" # Deprecated
        IdIsInvalid = "91610"
        IdIsNotAllowed = "91611"
        IdIsRequired = "91613"
        IdIsTooLong = "91612"
        LastNameIsTooLong = "81613"
        PhoneIsTooLong = "81614"
        VaultedPaymentInstrumentNonceBelongsToDifferentCustomer = "91617"
        WebsiteIsInvalid = WebsiteFormatIsInvalid = "81616"
        WebsiteIsTooLong = "81615"

    class Descriptor(object):
        DynamicDescriptorsDisabled = "92203"
        InternationalNameFormatIsInvalid = "92204"
        InternationalPhoneFormatIsInvalid = "92205"
        NameFormatIsInvalid = "92201"
        PhoneFormatIsInvalid = "92202"
        UrlFormatIsInvalid = "92206"

    class Dispute(object):
        CanOnlyAddEvidenceToOpenDispute = "95701"
        CanOnlyRemoveEvidenceFromOpenDispute = "95702"
        CanOnlyAddEvidenceDocumentToDispute = "95703"
        CanOnlyAcceptOpenDispute = "95704"
        CanOnlyFinalizeOpenDispute = "95705"

    class DocumentUpload(object):
        KindIsInvalid = "84901"
        FileIsTooLarge = "84902"
        FileTypeIsInvalid = "84903"
        FileIsMalformedOrEncrypted = "84904"

    class Merchant(object):
        CountryCannotBeBlank = "83603"
        CountryCodeAlpha2IsInvalid = "93607"
        CountryCodeAlpha2IsNotAccepted = "93606"
        CountryCodeAlpha3IsInvalid = "93605"
        CountryCodeAlpha3IsNotAccepted = "93604"
        CountryCodeNumericIsInvalid = "93609"
        CountryCodeNumericIsNotAccepted = "93608"
        CountryNameIsInvalid = "93611"
        CountryNameIsNotAccepted = "93610"
        CurrenciesAreInvalid = "93614"
        EmailFormatIsInvalid = "93602"
        EmailIsRequired = "83601"
        InconsistentCountry = "93612"
        PaymentMethodsAreInvalid = "93613"
        PaymentMethodsAreNotAllowed = "93615"
        MerchantAccountExistsForCurrency = "93616"
        CurrencyIsRequired = "93617"
        CurrencyIsInvalid = "93618"
        NoMerchantAccounts = "93619"
        MerchantAccountExistsForId = "93620"

    class MerchantAccount(object):
        IdFormatIsInvalid = "82603"
        IdIsInUse = "82604"
        IdIsNotAllowed = "82605"
        IdIsTooLong = "82602"
        MasterMerchantAccountIdIsInvalid = "82607"
        MasterMerchantAccountIdIsRequired = "82606"
        MasterMerchantAccountMustBeActive = "82608"
        TosAcceptedIsRequired = "82610"
        CannotBeUpdated = "82674"
        IdCannotBeUpdated = "82675"
        MasterMerchantAccountIdCannotBeUpdated = "82676"
        Declined = "82626"
        DeclinedMasterCardMatch = "82622"
        DeclinedOFAC = "82621"
        DeclinedFailedKYC = "82623"
        DeclinedSsnInvalid = "82624"
        DeclinedSsnMatchesDeceased = "82625"

        class ApplicantDetails(object):
            AccountNumberIsRequired = "82614"
            CompanyNameIsInvalid = "82631"
            CompanyNameIsRequiredWithTaxId = "82633"
            DateOfBirthIsRequired = "82612"
            Declined = "82626" # Keep for backwards compatibility
            DeclinedMasterCardMatch = "82622" # Keep for backwards compatibility
            DeclinedOFAC = "82621" # Keep for backwards compatibility
            DeclinedFailedKYC = "82623" # Keep for backwards compatibility
            DeclinedSsnInvalid = "82624" # Keep for backwards compatibility
            DeclinedSsnMatchesDeceased = "82625" # Keep for backwards compatibility
            EmailAddressIsInvalid = "82616"
            FirstNameIsInvalid = "82627"
            FirstNameIsRequired = "82609"
            LastNameIsInvalid = "82628"
            LastNameIsRequired = "82611"
            PhoneIsInvalid = "82636"
            RoutingNumberIsInvalid = "82635"
            RoutingNumberIsRequired = "82613"
            SsnIsInvalid = "82615"
            TaxIdIsInvalid = "82632"
            TaxIdIsRequiredWithCompanyName = "82634"
            DateOfBirthIsInvalid = "82663"
            EmailAddressIsRequired = "82665"
            AccountNumberIsInvalid = "82670"
            TaxIdMustBeBlank = "82673"

            class Address(object):
                LocalityIsRequired = "82618"
                PostalCodeIsInvalid = "82630"
                PostalCodeIsRequired = "82619"
                RegionIsRequired = "82620"
                StreetAddressIsInvalid = "82629"
                StreetAddressIsRequired = "82617"
                RegionIsInvalid = "82664"

        class Individual(object):
            FirstNameIsRequired = "82637"
            LastNameIsRequired = "82638"
            DateOfBirthIsRequired = "82639"
            SsnIsInvalid = "82642"
            EmailAddressIsInvalid = "82643"
            FirstNameIsInvalid = "82644"
            LastNameIsInvalid = "82645"
            PhoneIsInvalid = "82656"
            DateOfBirthIsInvalid = "82666"
            EmailAddressIsRequired = "82667"

            class Address(object):
                StreetAddressIsRequired = "82657"
                LocalityIsRequired = "82658"
                PostalCodeIsRequired = "82659"
                RegionIsRequired = "82660"
                StreetAddressIsInvalid = "82661"
                PostalCodeIsInvalid = "82662"
                RegionIsInvalid = "82668"

        class Business(object):
            DbaNameIsInvalid = "82646"
            LegalNameIsInvalid = "82677"
            LegalNameIsRequiredWithTaxId = "82669"
            TaxIdIsInvalid = "82647"
            TaxIdIsRequiredWithLegalName = "82648"
            TaxIdMustBeBlank = "82672"
            class Address(object):
                StreetAddressIsInvalid = "82685"
                PostalCodeIsInvalid = "82686"
                RegionIsInvalid = "82684"

        class Funding(object):
            RoutingNumberIsRequired = "82640"
            AccountNumberIsRequired = "82641"
            RoutingNumberIsInvalid = "82649"
            AccountNumberIsInvalid = "82671"
            DestinationIsInvalid = "82679"
            DestinationIsRequired = "82678"
            EmailAddressIsInvalid = "82681"
            EmailAddressIsRequired = "82680"
            MobilePhoneIsInvalid = "82683"
            MobilePhoneIsRequired = "82682"

    class OAuth(object):
        InvalidGrant = "93801"
        InvalidCredentials = "93802"
        InvalidScope = "93803"
        InvalidRequest = "93804"
        UnsupportedGrantType = "93805"

    class Verification(object):
        class Options(object):
            AmountCannotBeNegative = "94201"
            AmountFormatIsInvalid = "94202"
            AmountIsTooLarge = "94207"
            AmountNotSupportedByProcessor = "94203"
            MerchantAccountIdIsInvalid = "94204"
            MerchantAccountIsSuspended = "94205"
            MerchantAccountIsForbidden = "94206"
            MerchantAccountCannotBeSubMerchantAccount = "94208"

    class PaymentMethod(object):
        CannotForwardPaymentMethodType = "93106"
        PaymentMethodParamsAreRequired = "93101"
        NonceIsInvalid = "93102"
        NonceIsRequired = "93103"
        CustomerIdIsRequired = "93104"
        CustomerIdIsInvalid = "93105"
        PaymentMethodNonceConsumed = "93107"
        PaymentMethodNonceUnknown = "93108"
        PaymentMethodNonceLocked = "93109"
        PaymentMethodNoLongerSupported = "93117"
        AuthExpired = "92911"
        CannotHaveFundingSourceWithoutAccessToken = "92912"
        InvalidFundingSourceSelection = "92913"
        CannotUpdatePayPalAccountUsingPaymentMethodNonce = "92914"

    class PayPalAccount(object):
        CannotHaveBothAccessTokenAndConsentCode = "82903"
        CannotVaultOneTimeUsePayPalAccount = "82902"
        ConsentCodeOrAccessTokenIsRequired = "82901"
        CustomerIdIsRequiredForVaulting = "82905"
        InvalidParamsForPayPalAccountUpdate = "92915"
        PayPalAccountsAreNotAccepted = "82904"
        PayPalCommunicationError = "92910"
        PaymentMethodNonceConsumed = "92907"
        PaymentMethodNonceLocked = "92909"
        PaymentMethodNonceUnknown = "92908"
        TokenIsInUse = "92906"

    class SettlementBatchSummary(object):
        CustomFieldIsInvalid = "82303"
        SettlementDateIsInvalid = "82302"
        SettlementDateIsRequired = "82301"

    class SEPAMandate(object):
        TypeIsRequired = "93304"
        IBANInvalidCharacter = "83305"
        BICInvalidCharacter = "83306"
        BICLengthIsInvalid = "83307"
        BICUnsupportedCountry = "83308"
        IBANUnsupportedCountry = "83309"
        IBANInvalidFormat = "83310"
        BillingAddressConflict = "93311"
        BillingAddressIdIsInvalid = "93312"
        TypeIsInvalid = "93313"

    class EuropeBankAccount(object):
        BICIsRequired = "83302"
        IBANIsRequired = "83303"
        AccountHolderNameIsRequired = "83301"

    class Subscription(object):
        BillingDayOfMonthCannotBeUpdated = "91918"
        BillingDayOfMonthIsInvalid = "91914"
        BillingDayOfMonthMustBeNumeric = "91913"
        CannotAddDuplicateAddonOrDiscount = "91911"
        CannotEditCanceledSubscription = "81901"
        CannotEditExpiredSubscription = "81910"
        CannotEditPriceChangingFieldsOnPastDueSubscription = "91920"
        FirstBillingDateCannotBeInThePast = "91916"
        FirstBillingDateCannotBeUpdated = "91919"
        FirstBillingDateIsInvalid = "91915"
        IdIsInUse = "81902"
        InconsistentNumberOfBillingCycles = "91908"
        InconsistentStartDate = "91917"
        InvalidRequestFormat = "91921"
        MerchantAccountDoesNotSupportInstrumentType = "91930"
        MerchantAccountIdIsInvalid = "91901"
        MismatchCurrencyISOCode = "91923"
        NumberOfBillingCyclesCannotBeBlank = "91912"
        NumberOfBillingCyclesIsTooSmall = "91909"
        NumberOfBillingCyclesMustBeGreaterThanZero = "91907"
        NumberOfBillingCyclesMustBeNumeric = "91906"
        PaymentMethodNonceCardTypeIsNotAccepted = "91924"
        PaymentMethodNonceInstrumentTypeDoesNotSupportSubscriptions = "91929"
        PaymentMethodNonceIsInvalid = "91925"
        PaymentMethodNonceNotAssociatedWithCustomer = "91926"
        PaymentMethodNonceUnvaultedCardIsNotAccepted = "91927"
        PaymentMethodTokenCardTypeIsNotAccepted = "91902"
        PaymentMethodTokenInstrumentTypeDoesNotSupportSubscriptions = "91928"
        PaymentMethodTokenIsInvalid = "91903"
        PaymentMethodTokenNotAssociatedWithCustomer = "91905"
        PlanBillingFrequencyCannotBeUpdated = "91922"
        PlanIdIsInvalid = "91904"
        PriceCannotBeBlank = "81903"
        PriceFormatIsInvalid = "81904"
        PriceIsTooLarge = "81923"
        StatusIsCanceled = "81905"
        TokenFormatIsInvalid = "81906"
        TrialDurationFormatIsInvalid = "81907"
        TrialDurationIsRequired = "81908"
        TrialDurationUnitIsInvalid = "81909"

        class Modification(object):
            AmountCannotBeBlank = "92003"
            AmountIsInvalid = "92002"
            AmountIsTooLarge = "92023"
            CannotEditModificationsOnPastDueSubscription = "92022"
            CannotUpdateAndRemove = "92015"
            ExistingIdIsIncorrectKind = "92020"
            ExistingIdIsInvalid = "92011"
            ExistingIdIsRequired = "92012"
            IdToRemoveIsIncorrectKind = "92021"
            IdToRemoveIsNotPresent = "92016"
            InconsistentNumberOfBillingCycles = "92018"
            InheritedFromIdIsInvalid = "92013"
            InheritedFromIdIsRequired = "92014"
            Missing = "92024"
            NumberOfBillingCyclesCannotBeBlank = "92017"
            NumberOfBillingCyclesIsInvalid = "92005"
            NumberOfBillingCyclesMustBeGreaterThanZero = "92019"
            QuantityCannotBeBlank = "92004"
            QuantityIsInvalid = "92001"
            QuantityMustBeGreaterThanZero = "92010"
            IdToRemoveIsInvalid = "92025"

    class Transaction(object):
        AmountCannotBeNegative = "81501"
        AmountDoesNotMatch3DSecureAmount = "91585"
        AmountDoesNotMatchIdealPaymentAmount = "915144"
        AmountIsInvalid = AmountFormatIsInvalid = "81503"
        AmountIsRequired = "81502"
        AmountIsTooLarge = "81528"
        AmountMustBeGreaterThanZero = "81531"
        BillingAddressConflict = "91530"
        CannotBeVoided = "91504"
        CannotCancelRelease = "91562"
        CannotCloneCredit = "91543"
        CannotCloneMarketplaceTransaction = "915137"
        CannotCloneTransactionWithPayPalAccount = "91573"
        CannotCloneTransactionWithVaultCreditCard = "91540"
        CannotCloneUnsuccessfulTransaction = "91542"
        CannotCloneVoiceAuthorizations = "91541"
        CannotHoldInEscrow = "91560"
        CannotPartiallyRefundEscrowedTransaction = "91563"
        CannotRefundCredit = "91505"
        CannotRefundSettlingTransaction = "91574"
        CannotRefundUnlessSettled = "91506"
        CannotRefundWithPendingMerchantAccount = "91559"
        CannotRefundWithSuspendedMerchantAccount = "91538"
        CannotReleaseFromEscrow = "91561"
        CannotSimulateTransactionSettlement = "91575"
        CannotSubmitForPartialSettlement = "915103"
        CannotSubmitForSettlement = "91507"
        CannotUpdateTransactionDetailsNotSubmittedForSettlement = "915129"
        ChannelIsTooLong = "91550"
        ChannelIsTooLong = "91550"
        CreditCardIsRequired = "91508"
        CustomFieldIsInvalid = "91526"
        CustomFieldIsTooLong = "81527"
        CustomerDefaultPaymentMethodCardTypeIsNotAccepted = "81509"
        CustomerDoesNotHaveCreditCard = "91511"
        CustomerIdIsInvalid = "91510"
        FailedAuthAdjustmentAllowRetry = "95603"
        FailedAuthAdjustmentHardDecline = "95602"
        FinalAuthSubmitForSettlementForDifferentAmount = "95601"
        HasAlreadyBeenRefunded = "91512"
        IdealPaymentNotComplete = "815141"
        IdealPaymentsCannotBeVaulted = "915150"
        MerchantAccountDoesNotMatch3DSecureMerchantAccount = "91584"
        MerchantAccountDoesNotMatchIdealPaymentMerchantAccount = "915143"
        MerchantAccountDoesNotSupportMOTO = "91558"
        MerchantAccountDoesNotSupportRefunds = "91547"
        MerchantAccountIdIsInvalid = "91513"
        MerchantAccountIsSusped = "91514" # Deprecated
        MerchantAccountIsSuspended = "91514"
        MerchantAccountNameIsInvalid = "91513" # Deprecated
        OrderIdDoesNotMatchIdealPaymentOrderId = "91503"
        OrderIdIsRequiredWithIdealPayment = "91502"
        OrderIdIsTooLong = "91501"
        PayPalAuthExpired = "91579"
        PayPalNotEnabled = "91576"
        PayPalVaultRecordMissingData = "91583"
        PaymentInstrumentNotSupportedByMerchantAccount = "91577"
        PaymentInstrumentTypeIsNotAccepted = "915101"
        PaymentMethodConflict = "91515"
        PaymentMethodConflictWithVenmoSDK = "91549"
        PaymentMethodDoesNotBelongToCustomer = "91516"
        PaymentMethodDoesNotBelongToSubscription = "91527"
        PaymentMethodNonceCardTypeIsNotAccepted = "91567"
        PaymentMethodNonceConsumed = "91564"
        PaymentMethodNonceHasNoValidPaymentInstrumentType = "91569"
        PaymentMethodNonceLocked = "91566"
        PaymentMethodNonceUnknown = "91565"
        PaymentMethodTokenCardTypeIsNotAccepted = "91517"
        PaymentMethodTokenIsInvalid = "91518"
        ProcessorAuthorizationCodeCannotBeSet = "91519"
        ProcessorAuthorizationCodeIsInvalid = "81520"
        ProcessorDoesNotSupportAuths = "915104"
        ProcessorDoesNotSupportCredits = "91546"
        ProcessorDoesNotSupportPartialSettlement = "915102"
        ProcessorDoesNotSupportUpdatingOrderId = "915107"
        ProcessorDoesNotSupportUpdatingDescriptor = "915108"
        ProcessorDoesNotSupportUpdatingTransactionDetails = "915130"
        ProcessorDoesNotSupportVoiceAuthorizations = "91545"
        PurchaseOrderNumberIsInvalid = "91548"
        PurchaseOrderNumberIsTooLong = "91537"
        RefundAmountIsTooLarge = "91521"
        ServiceFeeAmountCannotBeNegative = "91554"
        ServiceFeeAmountFormatIsInvalid = "91555"
        ServiceFeeAmountIsTooLarge = "91556"
        ServiceFeeAmountNotAllowedOnMasterMerchantAccount = "91557"
        ServiceFeeIsNotAllowedOnCredits = "91552"
        ServiceFeeNotAcceptedForPayPal = "91578"
        SettlementAmountIsLessThanServiceFeeAmount = "91551"
        SettlementAmountIsTooLarge = "91522"
        ShippingAddressDoesntMatchCustomer = "91581"
        SubMerchantAccountRequiresServiceFeeAmount = "91553"
        SubscriptionDoesNotBelongToCustomer = "91529"
        SubscriptionIdIsInvalid = "91528"
        SubscriptionStatusMustBePastDue = "91531"
        TaxAmountCannotBeNegative = "81534"
        TaxAmountFormatIsInvalid = "81535"
        TaxAmountIsTooLarge = "81536"
        ThreeDSecureAuthenticationFailed = "81571"
        ThreeDSecureTokenIsInvalid = "91568"
        ThreeDSecureTransactionDataDoesntMatchVerify = "91570"
        ThreeDSecureEciFlagIsRequired = "915113"
        ThreeDSecureCavvIsRequired = "915116"
        ThreeDSecureXidIsRequired = "915115"
        ThreeDSecureEciFlagIsInvalid = "915114"
        ThreeDSecureMerchantAccountDoesNotSupportCardType = "915131"
        TypeIsInvalid = "91523"
        TypeIsRequired = "91524"
        UnsupportedVoiceAuthorization = "91539"

        class Options(object):
            SubmitForSettlementIsRequiredForCloning = "91544"
            SubmitForSettlementIsRequiredForPayPalUnilateral = "91582"
            UseBillingForShippingDisabled = "91572"
            VaultIsDisabled = "91525"

            class PayPal(object):
                CustomFieldTooLong = "91580"

        class Industry(object):
            IndustryTypeIsInvalid = "93401"

            class Lodging(object):
                EmptyData = "93402"
                FolioNumberIsInvalid = "93403"
                CheckInDateIsInvalid = "93404"
                CheckOutDateIsInvalid = "93405"
                CheckOutDateMustFollowCheckInDate = "93406"
                UnknownDataField = "93407"
            class TravelCruise(object):
                EmptyData = "93408"
                UnknownDataField = "93409"
                TravelPackageIsInvalid = "93410"
                DepartureDateIsInvalid = "93411"
                LodgingCheckInDateIsInvalid = "93412"
                LodgingCheckOutDateIsInvalid = "93413"
